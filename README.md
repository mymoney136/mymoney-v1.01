# GlassBudget — Prototype (HTML + Python)

This workspace contains a minimal prototype frontend (`index.html`) and a small Python server (`app.py`) which serves the page and provides a safe `/config` endpoint that reads from a local `.env` file.

Files added:
- `index.html` — glass-style frontend skeleton
- `app.py` — Flask server serving `index.html` and `/config`
- `.env.example` — example env file with placeholders
- `requirements.txt` — Python dependencies

Quick start (Windows PowerShell):

1. Create and activate a virtual environment:

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and edit the file to add your `SUPABASE_URL` and `SUPABASE_ANON_KEY`.

4. Run the server:

```
python app.py
```

5. Open `http://127.0.0.1:8000` in your browser.

Security note: the server does not expose the anon key by default. If you set `ALLOW_EXPOSE_KEYS=1` in `.env` the `/config` endpoint will return the full values — only enable for local development if you understand the risks.

Publishing to GitHub
--------------------

Before publishing, ensure you DO NOT commit secrets. This repo includes a `.gitignore` which ignores `.env` by default. Verify your local `.env` is not staged.

Quick CLI steps to publish (PowerShell):

```powershell
# initialize repo (if not already a git repo)
git init
git add .gitignore
git add -A
git commit -m "Initial prototype: GlassBudget frontend + server"

# create a remote GitHub repo and add it as `origin` OR use the GitHub extension UI to create/push
# Replace <your-remote-url> with the HTTPS/SSH URL from GitHub
git remote add origin <your-remote-url>
git branch -M main
git push -u origin main
```

If you accidentally committed `.env` or secrets, remove them from the index (this does NOT remove them from history):

```powershell
git rm --cached .env
git commit -m "Remove .env from repository"
git push origin main
```

If `.env` or keys were already pushed and you need to purge them from history, use a history-rewrite tool (e.g. `git filter-repo` or the BFG Repo-Cleaner) — I can provide commands for that if needed. After rewriting history you'll need to force-push and rotate any exposed keys.

Using the GitHub extension in VS Code
-----------------------------------
- Open the Source Control view or the GitHub extension.
- Sign in to GitHub from the extension (if not already signed in).
- Use the extension's "Create Repository" or "Publish to GitHub" flow to create a remote and push your local repo. The extension will guide you through adding a remote and pushing.

Security reminder: never paste real secret keys into GitHub issues or public chats. Keep `.env` local and prefer using CI secrets or GitHub Secrets for deployment keys.
