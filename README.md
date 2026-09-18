# Learning Hub

A very simple Flask website: sign in with Google, pick a subject (Maths, Physics,
Computer Science), work through short lessons, and take a quiz after each one.
Quizzes give a remark based on your score and unlock the next lesson if you pass (60%+).

## Project structure

```
learning-hub/
├── app.py              # Flask routes, auth, quiz grading
├── content.py           # All lesson text and quiz questions (edit this to add content)
├── requirements.txt
├── .env.example          # Copy to .env and fill in your own values
├── templates/            # HTML pages (Jinja2)
├── static/style.css       # Plain CSS
└── database.db            # Created automatically on first run (SQLite)
```

## 1. Get Google OAuth credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a project
   (or use an existing one).
2. Go to **APIs & Services > OAuth consent screen** and set it up (External is fine for testing).
3. Go to **APIs & Services > Credentials > Create Credentials > OAuth client ID**.
4. Choose **Web application**.
5. Under **Authorized redirect URIs**, add:
   - `http://localhost:5000/callback` (for local testing)
   - Your production URL + `/callback` once you deploy (e.g. `https://yourapp.onrender.com/callback`)
6. Copy the **Client ID** and **Client Secret**.

## 2. Set up locally

```bash
cd learning-hub
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# then edit .env and paste in your Google Client ID, Client Secret,
# and any random string for FLASK_SECRET_KEY
```

## 3. Run it

```bash
python app.py
```

Visit `http://localhost:5000`, sign in with Google, and start a subject.

The SQLite file `database.db` is created automatically and stores users and progress.

## 4. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

`.env` and `database.db` are already excluded via `.gitignore`, so your secrets and
personal data won't be uploaded.

## 5. Deploying to Render

This repo includes `render.yaml`, `Procfile`, and a `gunicorn` entry, so it deploys with
almost no manual setup.

**Option A — Blueprint (recommended, uses `render.yaml`):**

1. Push this repo to GitHub.
2. In the [Render dashboard](https://dashboard.render.com/), click **New > Blueprint**
   and select your repo. Render reads `render.yaml` and creates the web service.
3. When prompted, fill in the two secret env vars: `GOOGLE_CLIENT_ID` and
   `GOOGLE_CLIENT_SECRET`. `FLASK_SECRET_KEY` is generated for you.
4. Deploy. Render gives you a URL like `https://learning-hub-xxxx.onrender.com`.
5. Back in Google Cloud Console (**Credentials > your OAuth client**), add
   `https://learning-hub-xxxx.onrender.com/callback` to **Authorized redirect URIs**.

**Option B — Manual web service (no Blueprint):**

1. **New > Web Service**, connect the repo.
2. Runtime: **Python 3**. Build command: `pip install -r requirements.txt`.
   Start command: `gunicorn app:app` (already set via `Procfile` too).
3. Under **Environment**, add `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, and a random
   `FLASK_SECRET_KEY`.
4. Add `https://<your-render-url>/callback` to Google Cloud Console's redirect URIs.

### About the database on Render

Render's default filesystem is **ephemeral** — anything written to disk (like the
SQLite file) is wiped on every deploy or restart. By default this repo runs fine on
Render's free plan, but user progress will reset each time you redeploy or the service
restarts, because the free plan doesn't support persistent disks.

If you upgrade to a paid Render plan and want progress to survive deploys:

- Using `render.yaml` (Option A): uncomment the `disk:` block and the `DB_PATH` env var
  in `render.yaml`, then redeploy the Blueprint.
- Manual setup (Option B): add a disk yourself (**Settings > Disks > Add Disk**, e.g.
  mount path `/opt/render/project/src/data`) and set an env var `DB_PATH` to
  `/opt/render/project/src/data/database.db`.

### Local development still works the same way

Locally, `DB_PATH` and `PORT` aren't set, so the app falls back to a `database.db` file
next to `app.py` and port 5000, and `FLASK_DEBUG` defaults to on. Run it with
`python app.py` as before — Render's `gunicorn app:app` start command is only used in
production.

## Adding more content

Open `content.py`. Each subject is a dictionary with a `name` and a list of `lessons`.
Each lesson needs a unique, consecutive `id` (lessons unlock in order: 1, then 2, then 3...),
a `title`, HTML `content`, and a `quiz` list of questions with `options` and the correct
`answer` index (0-based). Just copy the pattern of an existing lesson.
