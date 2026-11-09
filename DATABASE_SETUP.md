# Making progress permanent (free Neon database)

Render's free plan wipes the app's disk on every deploy and restart, so progress stored in a local
file is lost. A Neon Postgres database lives outside Render, so nothing is lost. Takes about 10 minutes.

## 1. Create the database
1. Go to https://neon.tech and sign up (free, you can use your Google or GitHub account).
2. Create a project. Name it `learning-hub`. Choose the region closest to your students.
3. When it opens, click **Connect** and copy the **connection string**. It looks like:
   `postgresql://username:password@ep-something.region.aws.neon.tech/neondb?sslmode=require`
   Keep it private. It is a password. Do not put it in GitHub.

## 2. Give it to Render
1. Render dashboard > your `learning-hub` service > **Environment**.
2. **Add Environment Variable**: key `DATABASE_URL`, value = the connection string. Save.
3. Push the updated code to GitHub (or click **Manual Deploy**). Render redeploys.
4. In the Render **Logs** you should see no line starting with `DATABASE ERROR`.

## 3. Check that it worked
1. Open your site, sign in, and pass one quiz.
2. In Render, click **Manual Deploy > Deploy latest commit** (or restart the service).
3. Sign in again. The lesson should still show as completed. If it does, you are done.

## If something is wrong
- `DATABASE ERROR` in the logs: the connection string is wrong or incomplete. Copy it again from Neon
  (the whole line, including `?sslmode=require`).
- The first page load after a quiet period can take 30-60 seconds. That is Render's free plan waking
  up (and Neon waking its database), not a data problem.
- Check Neon's current free-plan limits on their pricing page, since these can change.
