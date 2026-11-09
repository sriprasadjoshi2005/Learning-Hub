import os
import random
import secrets
import sqlite3
from datetime import datetime
from functools import wraps

from flask import Flask, render_template, redirect, url_for, session, request, abort
from werkzeug.middleware.proxy_fix import ProxyFix
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv

from content_loader import load_all, LEVEL_LABELS

load_dotenv()

app = Flask(__name__)

_secret = os.environ.get("FLASK_SECRET_KEY")
if not _secret:
    print("WARNING: FLASK_SECRET_KEY is not set; using a temporary key (logins reset on restart).")
    _secret = secrets.token_hex(32)
app.secret_key = _secret

# Render terminates HTTPS at a proxy; without this Flask builds http:// OAuth redirect URIs.
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

DB_PATH = os.environ.get("DB_PATH", os.path.join(os.path.dirname(__file__), "database.db"))
# With DATABASE_URL set (Neon/Postgres) progress survives restarts and redeploys.
# Without it, the app uses the local SQLite file (fine for testing on your own computer).
DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()
USE_PG = bool(DATABASE_URL)
if USE_PG:
    import psycopg
    from psycopg.rows import dict_row
PASS_MARK = 60
# "sequential": pass a lesson's quiz to unlock the next.  "open": every lesson is available.
UNLOCK_MODE = os.environ.get("UNLOCK_MODE", "sequential").lower()

SUBJECTS, CONTENT_ERRORS = load_all()
for _err in CONTENT_ERRORS:
    print("CONTENT ERROR (lesson skipped):", _err)

oauth = OAuth(app)
google = oauth.register(
    name="google",
    client_id=os.environ.get("GOOGLE_CLIENT_ID"),
    client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


# ---------- database ----------

class DB:
    """Same small interface for SQLite and Postgres: execute / commit / close.
    SQL is written with ? placeholders; they are translated for Postgres."""

    def __init__(self):
        if USE_PG:
            self.conn = psycopg.connect(DATABASE_URL, row_factory=dict_row, connect_timeout=15)
        else:
            self.conn = sqlite3.connect(DB_PATH)
            self.conn.row_factory = sqlite3.Row

    def execute(self, sql, params=()):
        if USE_PG:
            sql = sql.replace("?", "%s")
        return self.conn.execute(sql, params)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()


def get_db():
    return DB()


def init_db():
    pk = "SERIAL PRIMARY KEY" if USE_PG else "INTEGER PRIMARY KEY AUTOINCREMENT"
    conn = get_db()
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS users (
            id {pk},
            google_id TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            name TEXT NOT NULL
        )
    """)
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS progress (
            id {pk},
            user_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            lesson_id INTEGER NOT NULL,
            completed INTEGER DEFAULT 0,
            score INTEGER DEFAULT 0,
            remark TEXT,
            updated_at TEXT,
            UNIQUE(user_id, subject, lesson_id)
        )
    """)
    conn.commit()
    conn.close()


def user_progress(subject_key=None):
    conn = get_db()
    if subject_key:
        rows = conn.execute("SELECT * FROM progress WHERE user_id = ? AND subject = ?",
                            (session["user_id"], subject_key)).fetchall()
    else:
        rows = conn.execute("SELECT * FROM progress WHERE user_id = ?", (session["user_id"],)).fetchall()
    conn.close()
    return rows


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return wrapper


def unlocked_ids(subject, completed_ids):
    """Set of lesson ids the student may open."""
    if UNLOCK_MODE == "open":
        return {l["id"] for l in subject["lessons"]}
    unlocked, open_next = set(), True
    for l in subject["lessons"]:
        if open_next:
            unlocked.add(l["id"])
        open_next = l["id"] in completed_ids
    return unlocked


def get_subject_or_404(key):
    subject = SUBJECTS.get(key)
    if not subject:
        abort(404)
    return subject


def get_lesson_or_404(subject, lesson_id):
    lesson = subject["by_id"].get(lesson_id)
    if not lesson:
        abort(404)
    return lesson


def remark_for(score_pct):
    if score_pct == 100:
        return "Perfect score! Excellent work."
    if score_pct >= 80:
        return "Great job, you know this well."
    if score_pct >= PASS_MARK:
        return "Good effort, you passed."
    if score_pct >= 40:
        return "Close, but review this lesson again."
    return "Keep practicing, revisit the lesson before retrying."


# ---------- auth ----------

@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    overview = [{"name": s["name"], "count": len(s["lessons"])} for s in SUBJECTS.values()]
    return render_template("index.html", overview=overview)


@app.route("/login")
def login():
    return google.authorize_redirect(url_for("callback", _external=True))


@app.route("/callback")
def callback():
    token = google.authorize_access_token()
    user_info = token.get("userinfo")
    if not user_info:
        user_info = google.get("https://openidconnect.googleapis.com/v1/userinfo").json()

    conn = get_db()
    row = conn.execute("SELECT * FROM users WHERE google_id = ?", (user_info["sub"],)).fetchone()
    if row is None:
        conn.execute("INSERT INTO users (google_id, email, name) VALUES (?, ?, ?)",
                     (user_info["sub"], user_info.get("email", ""), user_info.get("name", "")))
        conn.commit()
        row = conn.execute("SELECT * FROM users WHERE google_id = ?", (user_info["sub"],)).fetchone()
    conn.close()

    session["user_id"] = row["id"]
    session["user_name"] = row["name"]
    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


# ---------- learning pages ----------

@app.route("/dashboard")
@login_required
def dashboard():
    rows = user_progress()
    done_by_subject = {}
    for r in rows:
        if r["completed"]:
            done_by_subject.setdefault(r["subject"], set()).add(r["lesson_id"])

    summary = []
    for key, subject in SUBJECTS.items():
        done_ids = done_by_subject.get(key, set())
        total = len(subject["lessons"])
        nxt = next((l for l in subject["lessons"] if l["id"] not in done_ids), None)
        summary.append({
            "key": key, "name": subject["name"], "description": subject["description"],
            "total": total, "done": len([l for l in subject["lessons"] if l["id"] in done_ids]),
            "next_id": nxt["id"] if nxt else None,
        })
    return render_template("dashboard.html", subjects=summary, user_name=session.get("user_name"))


@app.route("/subject/<subject_key>")
@login_required
def subject_view(subject_key):
    subject = get_subject_or_404(subject_key)
    rows = user_progress(subject_key)
    completed = {r["lesson_id"] for r in rows if r["completed"]}
    best = {r["lesson_id"]: r["score"] for r in rows}
    open_ids = unlocked_ids(subject, completed)

    lessons = [{
        "id": l["id"], "title": l["title"], "level": l["level"],
        "level_label": LEVEL_LABELS.get(l["level"], ""),
        "completed": l["id"] in completed, "unlocked": l["id"] in open_ids,
        "best": best.get(l["id"]),
    } for l in subject["lessons"]]
    return render_template("subject.html", subject_key=subject_key, subject_name=subject["name"], lessons=lessons)


def _guard(subject_key, lesson_id):
    """Returns (subject, lesson) or a redirect response if the lesson is still locked."""
    subject = get_subject_or_404(subject_key)
    lesson = get_lesson_or_404(subject, lesson_id)
    completed = {r["lesson_id"] for r in user_progress(subject_key) if r["completed"]}
    if lesson_id not in unlocked_ids(subject, completed):
        return subject, None
    return subject, lesson


@app.route("/lesson/<subject_key>/<int:lesson_id>")
@login_required
def lesson_view(subject_key, lesson_id):
    subject, lesson = _guard(subject_key, lesson_id)
    if lesson is None:
        return redirect(url_for("subject_view", subject_key=subject_key))
    return render_template("lesson.html", subject_key=subject_key, subject_name=subject["name"], lesson=lesson,
                           level_label=LEVEL_LABELS.get(lesson["level"], ""),
                           prev_id=lesson_id - 1 if lesson_id - 1 in subject["by_id"] else None,
                           next_id=lesson_id + 1 if lesson_id + 1 in subject["by_id"] else None)


@app.route("/quiz/<subject_key>/<int:lesson_id>", methods=["GET", "POST"])
@login_required
def quiz_view(subject_key, lesson_id):
    subject, lesson = _guard(subject_key, lesson_id)
    if lesson is None:
        return redirect(url_for("subject_view", subject_key=subject_key))

    questions = lesson["quiz"]

    if request.method == "GET":
        shown = []
        for q in questions:
            order = list(range(len(q["options"])))
            random.shuffle(order)  # display order only; the form still submits the original index
            shown.append({"question": q["question"], "options": [(i, q["options"][i]) for i in order]})
        return render_template("quiz.html", subject_key=subject_key, subject_name=subject["name"],
                               lesson=lesson, shown=shown)

    review, correct = [], 0
    for i, q in enumerate(questions):
        try:
            picked = int(request.form.get("q%d" % i, ""))
        except ValueError:
            picked = None
        if picked is not None and not 0 <= picked < len(q["options"]):
            picked = None
        is_right = picked == q["answer"]
        correct += is_right
        review.append({
            "question": q["question"], "options": q["options"], "picked": picked,
            "answer": q["answer"], "right": is_right, "explanation": q["explanation"],
        })

    score_pct = round(correct / len(questions) * 100)
    passed = score_pct >= PASS_MARK
    remark = remark_for(score_pct)

    # Progress only ever improves: a failed retake never undoes a pass or lowers the best score.
    conn = get_db()
    conn.execute(
        """
        INSERT INTO progress (user_id, subject, lesson_id, completed, score, remark, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(user_id, subject, lesson_id) DO UPDATE SET
            completed = CASE WHEN excluded.completed > progress.completed THEN excluded.completed ELSE progress.completed END,
            remark = CASE WHEN excluded.score >= progress.score THEN excluded.remark ELSE progress.remark END,
            score = CASE WHEN excluded.score > progress.score THEN excluded.score ELSE progress.score END,
            updated_at = excluded.updated_at
        """,
        (session["user_id"], subject_key, lesson_id, int(passed), score_pct, remark, datetime.utcnow().isoformat()),
    )
    conn.commit()
    best = conn.execute("SELECT score FROM progress WHERE user_id = ? AND subject = ? AND lesson_id = ?",
                        (session["user_id"], subject_key, lesson_id)).fetchone()["score"]
    conn.close()

    return render_template(
        "result.html", subject_key=subject_key, subject_name=subject["name"], lesson=lesson,
        score=score_pct, best=best, correct=correct, total=len(questions), remark=remark, passed=passed,
        review=review, next_lesson=subject["by_id"].get(lesson_id + 1),
    )


@app.errorhandler(404)
def not_found(_):
    return render_template("404.html"), 404


# Runs on import too, so the tables exist under gunicorn (Render).
try:
    init_db()
except Exception as exc:
    print("DATABASE ERROR: could not connect or create tables. Check DATABASE_URL.", exc)
    raise

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
