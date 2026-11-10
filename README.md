# Learning Hub

A Flask site: sign in with Google, pick a subject, read short lessons, and take a quiz after each one.
Quizzes show the correct answer and an explanation for every question. Passing (60%+) unlocks the next lesson. Students can also skip a quiz: the next lesson opens, the skipped lesson is labelled "Skipped" (not "Completed"), and they can still take the quiz later.
Your best score is kept; a failed retake never undoes a pass.

## Project structure

```
app.py              Flask routes, login, quiz grading
content_loader.py   Reads lessons from content/ (and the old content.py, if it is still there)
check_content.py    Validates every lesson. Run it before every push.
content/            One folder per subject, one Markdown file per lesson
templates/, static/ Pages and styling
```

## Run locally

```bash
pip install -r requirements.txt
cp .env.example .env        # fill in Google keys and a random FLASK_SECRET_KEY
python check_content.py
python app.py
```

## Adding or editing lessons

Create `content/<subject>/NN-topic-name.md` (numbers run 01, 02, 03... with no gaps).
A new subject is a new folder with a `_subject.md` (name, description, order).

```
---
title: Quadratic Equations
level: intermediate
---

Lesson text in Markdown. Write maths with $x^2$ inline or $$x = \frac{-b}{2a}$$ on its own line.
Write a literal dollar sign as \$.

## Quiz

1. Question text?
   - [ ] wrong option
   - [x] correct option (exactly one)
   - [ ] wrong option
   - [ ] wrong option
   > Explanation shown after the quiz.
```

Rules (enforced by `check_content.py`): level is `foundation`, `intermediate`, `advanced` or `exam`;
2 or 3 questions per lesson; exactly 4 options and one `[x]`; every question has an explanation.
Options are shuffled on screen, so the position of the correct answer in the file does not matter.

A folder in `content/` replaces an old subject with the same name in `content.py`.

## Settings (environment variables)

| Name | Purpose |
|---|---|
| `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET` | Google login |
| `FLASK_SECRET_KEY` | Signs login sessions (Render generates it) |
| `UNLOCK_MODE` | `sequential` (default) or `open` (all lessons available) |
| `ALLOW_SKIP` | `true` (default) lets students skip a quiz and move on; `false` turns the option off |
| `DATABASE_URL` | Neon/Postgres connection string. When set, progress is stored there (permanent). |
| `DB_PATH` | Location of the local SQLite file, used only when `DATABASE_URL` is empty |

## Render and the database

On Render's free plan the disk is wiped on every deploy and restart, so a local SQLite file loses progress.
Set `DATABASE_URL` to a free Neon Postgres database and progress is permanent. Follow `DATABASE_SETUP.md`.
Without `DATABASE_URL` the app still works, using a local SQLite file (fine for testing on your computer).
