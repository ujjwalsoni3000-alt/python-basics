# Push this project to GitHub

1. Create an EMPTY repository on GitHub (no README, no .gitignore, no license):
   https://github.com/new  -> name it `python-basics`

2. Open a terminal inside this folder and run:

```bash
git init
git add .
git commit -m "Initial commit: Python basics lessons"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/python-basics.git
git push -u origin main
```

3. Replace `YOUR-USERNAME` with your GitHub username (also in README.md),
   and `YOUR NAME` in LICENSE.

If GitHub asks for a password, use a Personal Access Token
(Settings -> Developer settings -> Personal access tokens) or sign in with GitHub CLI: `gh auth login`.
