# Restoring Full Project to GitHub

## The Problem

Only the `mobile/` folder is visible in your GitHub repo instead of the whole project.

## Check What Happened

### Step 1: Check Current Directory

```bash
cd "e:\Educational\Heidelberg Image\rock-dashboard-master"
pwd  # or 'cd' in PowerShell
```

Make sure you're in the **project root**, not inside `mobile/`.

### Step 2: Check Git Status

```bash
git status
```

This shows what files Git is tracking.

### Step 3: Check What's in Git

```bash
git ls-files
```

This lists all files tracked by Git.

---

## Fix: Add All Files

### Option 1: Add Everything (Recommended)

```bash
# Make sure you're in project root
cd "e:\Educational\Heidelberg Image\rock-dashboard-master"

# Add all files (including Flask app)
git add .

# Check what will be committed
git status

# Commit
git commit -m "Add full project including Flask backend and mobile app"

# Push
git push origin master
```

### Option 2: Add Specific Folders

If Option 1 doesn't work, add files manually:

```bash
# Add Flask backend files
git add app.py
git add config.py
git add requirements.txt
git add limestone/
git add Procfile
git add README.md

# Add mobile folder (if not already)
git add mobile/

# Commit
git commit -m "Add full project files"

# Push
git push origin master
```

---

## Check What's Tracked

### See all tracked files:

```bash
git ls-files
```

### See what's NOT tracked:

```bash
git status
```

Files in red are not tracked.

---

## Common Causes

1. **Git initialized in wrong directory**
   - Should be in: `rock-dashboard-master/`
   - Not in: `rock-dashboard-master/mobile/`

2. **Files ignored by .gitignore**
   - Check if `limestone/`, `app.py`, etc. are being ignored
   - Run: `git check-ignore -v app.py` to see if it's ignored

3. **Wrong repository**
   - Make sure you're pushing to the right repo

---

## Full Project Structure Should Look Like:

```
rock-dashboard-master/          # Git root here
├── .git/                        # Git folder
├── app.py
├── config.py
├── requirements.txt
├── Procfile
├── README.md
├── limestone/
│   ├── __init__.py
│   ├── database.py
│   ├── routes/
│   ├── templates/
│   └── ...
└── mobile/                      # Mobile app
    ├── App.js
    ├── package.json
    └── ...
```

---

## Quick Fix Commands

Run these in order:

```bash
# 1. Navigate to project root
cd "e:\Educational\Heidelberg Image\rock-dashboard-master"

# 2. Check current status
git status

# 3. Add all files
git add .

# 4. Check what will be committed
git status

# 5. Commit everything
git commit -m "Restore full project with Flask backend and mobile app"

# 6. Push
git push origin master
```

---

## Verify on GitHub

After pushing, check GitHub:
- ✅ `app.py` should be visible
- ✅ `limestone/` folder should be visible
- ✅ `mobile/` folder should be visible
- ✅ `requirements.txt`, `Procfile`, etc. should be visible

---

## If Files Still Don't Appear

### Check .gitignore

Maybe files are being ignored. Check:

```bash
# Check if file is ignored
git check-ignore -v app.py
git check-ignore -v limestone/

# View .gitignore
cat .gitignore
```

If important files are in `.gitignore`, remove them or comment them out.

### Force Add Ignored Files

```bash
git add -f app.py
git add -f limestone/
```

Then commit and push.

---

## After This Works

Your repo should show:
- ✅ Flask backend files
- ✅ Mobile app files
- ✅ Complete project structure

