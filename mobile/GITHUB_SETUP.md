# Adding Mobile Folder to GitHub

## Option 1: Using GitHub Web Interface (Easiest)

### Steps:

1. **Go to your GitHub repository** on GitHub.com

2. **Click "Add file" → "Upload files"**

3. **Drag and drop the entire `mobile/` folder**
   - Or click "choose your files" and select the mobile folder

4. **Important:** Make sure you're in the root of your repo (not inside mobile folder)

5. **Add a commit message:**
   ```
   Add mobile app (React Native + Expo)
   ```

6. **Click "Commit changes"**

### What Gets Uploaded:

✅ All files in `mobile/` folder
- `App.js`, `index.js`, `package.json`
- `components/`, `config/`, `navigation/`
- Documentation files
- `.gitignore` will automatically exclude `node_modules/`

❌ Won't upload (automatically excluded):
- `node_modules/` (already in `.gitignore`)
- `.env` files
- Build artifacts

---

## Option 2: Using Git Commands (Recommended)

This is better for future updates!

### First Time Setup:

1. **Navigate to your project root** (one level above mobile):
   ```bash
   cd e:\Educational\Heidelberg Image\rock-dashboard-master
   ```

2. **Check if git is initialized:**
   ```bash
   git status
   ```
   If it says "not a git repository", initialize it:
   ```bash
   git init
   git remote add origin https://github.com/yourusername/your-repo-name.git
   ```

3. **Add mobile folder:**
   ```bash
   git add mobile/
   ```

4. **Commit:**
   ```bash
   git commit -m "Add mobile app (React Native + Expo)"
   ```

5. **Push to GitHub:**
   ```bash
   git push origin main
   ```
   (or `master` if that's your branch name)

### Future Updates:

When you make changes to the mobile app:

```bash
cd e:\Educational\Heidelberg Image\rock-dashboard-master
git add mobile/
git commit -m "Update mobile app: [description]"
git push
```

---

## Recommended Project Structure

After adding, your repo structure will look like:

```
rock-dashboard-master/
├── app.py                  # Flask backend
├── config.py
├── requirements.txt
├── limestone/
│   ├── routes/
│   ├── templates/
│   └── ...
├── mobile/                 # ← New mobile app folder
│   ├── App.js
│   ├── package.json
│   ├── components/
│   ├── config/
│   └── ...
├── README.md
└── .gitignore
```

---

## Important: Update .gitignore

Make sure your root `.gitignore` includes mobile-specific ignores:

```gitignore
# Mobile app
mobile/node_modules/
mobile/.expo/
mobile/.expo-shared/
mobile/dist/
mobile/build/
mobile/android/app/build/
mobile/ios/build/
```

Or create `mobile/.gitignore` if it doesn't exist (you already have one ✅).

---

## Quick Check After Upload

After uploading, verify on GitHub:

1. ✅ `mobile/` folder appears in repository
2. ✅ `mobile/package.json` is visible
3. ✅ `mobile/App.js` is visible
4. ✅ Documentation files are there
5. ❌ No `node_modules/` visible (correctly ignored)

---

## Tips

### Using GitHub Web (First time):
- ✅ Easiest for first upload
- ❌ Harder for future updates (need to upload files one by one)

### Using Git Commands (Future updates):
- ✅ Better for regular updates
- ✅ Version control history
- ✅ Easy to rollback changes

**Recommendation:** Use GitHub web for the first upload, then switch to Git commands for future updates!

---

## If You Get Errors

### "File too large"
- Make sure `node_modules/` is in `.gitignore`
- Don't upload build folders

### "Authentication required"
- Use Git commands instead, or
- Set up GitHub CLI or SSH keys

### "Can't find repository"
- Check you're logged into GitHub
- Verify repository URL is correct

