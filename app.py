import os
import sqlite3
from datetime import datetime
from functools import wraps

from flask import Flask, render_template, redirect, url_for, session, request, abort
from werkzeug.middleware.proxy_fix import ProxyFix
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv

from content import SUBJECTS

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key-change-me")

# Render (like most hosts) puts the app behind a reverse proxy that terminates HTTPS.
# Without this, Flask thinks every request is plain HTTP and builds http:// redirect
# URIs for Google OAuth, which then won't match what's registered in Google Cloud Console.
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

DB_PATH = os.environ.get("DB_PATH", os.path.join(os.path.dirname(__file__), "database.db"))

oauth = OAuth(app)
google = oauth.register(
    name="google",
    client_id=os.environ.get("GOOGLE_CLIENT_ID"),
    client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


# ---------- database helpers ----------

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            google_id TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            name TEXT NOT NULL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return wrapper


# ---------- auth routes ----------

@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")


@app.route("/login")
def login():
    redirect_uri = url_for("callback", _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route("/callback")
def callback():
    token = google.authorize_access_token()
    user_info = token.get("userinfo")
    if not user_info:
        user_info = google.get("https://openidconnect.googleapis.com/v1/userinfo").json()

    conn = get_db()
    row = conn.execute("SELECT * FROM users WHERE google_id = ?", (user_info["sub"],)).fetchone()
    if row is None:
        conn.execute(
            "INSERT INTO users (google_id, email, name) VALUES (?, ?, ?)",
            (user_info["sub"], user_info.get("email", ""), user_info.get("name", "")),
        )
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


# ---------- app routes ----------

@app.route("/dashboard")
@login_required
def dashboard():
    conn = get_db()
    progress_rows = conn.execute(
        "SELECT * FROM progress WHERE user_id = ?", (session["user_id"],)
    ).fetchall()
    conn.close()

    completed_lookup = {(r["subject"], r["lesson_id"]) for r in progress_rows if r["completed"]}

    subjects_summary = []
    for key, subject in SUBJECTS.items():
        total = len(subject["lessons"])
        done = sum(1 for l in subject["lessons"] if (key, l["id"]) in completed_lookup)
        subjects_summary.append({"key": key, "name": subject["name"], "total": total, "done": done})

    return render_template("dashboard.html", subjects=subjects_summary, user_name=session.get("user_name"))


@app.route("/subject/<subject_key>")
@login_required
def subject_view(subject_key):
    subject = SUBJECTS.get(subject_key)
    if not subject:
        abort(404)

    conn = get_db()
    progress_rows = conn.execute(
        "SELECT * FROM progress WHERE user_id = ? AND subject = ?",
        (session["user_id"], subject_key),
    ).fetchall()
    conn.close()

    completed_ids = {r["lesson_id"] for r in progress_rows if r["completed"]}

    lessons = []
    unlocked = True
    for lesson in subject["lessons"]:
        lessons.append({
            "id": lesson["id"],
            "title": lesson["title"],
            "completed": lesson["id"] in completed_ids,
            "unlocked": unlocked,
        })
        if lesson["id"] not in completed_ids:
            unlocked = False

    return render_template("subject.html", subject_key=subject_key, subject_name=subject["name"], lessons=lessons)


@app.route("/lesson/<subject_key>/<int:lesson_id>")
@login_required
def lesson_view(subject_key, lesson_id):
    subject = SUBJECTS.get(subject_key)
    if not subject:
        abort(404)
    lesson = next((l for l in subject["lessons"] if l["id"] == lesson_id), None)
    if not lesson:
        abort(404)
    return render_template("lesson.html", subject_key=subject_key, subject_name=subject["name"], lesson=lesson)


@app.route("/quiz/<subject_key>/<int:lesson_id>", methods=["GET", "POST"])
@login_required
def quiz_view(subject_key, lesson_id):
    subject = SUBJECTS.get(subject_key)
    if not subject:
        abort(404)
    lesson = next((l for l in subject["lessons"] if l["id"] == lesson_id), None)
    if not lesson:
        abort(404)

    if request.method == "GET":
        return render_template("quiz.html", subject_key=subject_key, subject_name=subject["name"], lesson=lesson)

    questions = lesson["quiz"]
    correct = 0
    for i, q in enumerate(questions):
        submitted = request.form.get(f"q{i}")
        if submitted is not None and int(submitted) == q["answer"]:
            correct += 1

    score_pct = round((correct / len(questions)) * 100)
    passed = score_pct >= 60

    if score_pct == 100:
        remark = "Perfect score! Excellent work."
    elif score_pct >= 80:
        remark = "Great job, you know this well."
    elif score_pct >= 60:
        remark = "Good effort, you passed."
    elif score_pct >= 40:
        remark = "Close, but you should review this lesson again."
    else:
        remark = "Keep practicing, revisit the lesson before retrying."

    conn = get_db()
    conn.execute(
        """
        INSERT INTO progress (user_id, subject, lesson_id, completed, score, remark, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(user_id, subject, lesson_id)
        DO UPDATE SET completed=excluded.completed, score=excluded.score,
                      remark=excluded.remark, updated_at=excluded.updated_at
        """,
        (session["user_id"], subject_key, lesson_id, int(passed), score_pct, remark, datetime.utcnow().isoformat()),
    )
    conn.commit()
    conn.close()

    next_lesson = next((l for l in subject["lessons"] if l["id"] == lesson_id + 1), None)

    return render_template(
        "result.html",
        subject_key=subject_key,
        subject_name=subject["name"],
        lesson=lesson,
        score=score_pct,
        correct=correct,
        total=len(questions),
        remark=remark,
        passed=passed,
        next_lesson=next_lesson,
    )


# Runs on import too, so the tables exist under gunicorn (Render), not just `python app.py`.
init_db()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
