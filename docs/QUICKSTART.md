# Quick Start Guide

Get started with Python Project Bundler in 5 minutes!

---

## 📥 Installation

### Option 1: Clone from GitHub
```bash
git clone https://github.com/Patisons/python-project-bundler.git
cd python-project-bundler
```

### Option 2: Download ZIP
1. Go to https://github.com/Patisons/python-project-bundler
2. Click green "Code" button → "Download ZIP"
3. Extract the archive
4. Navigate to the folder

---

## ▶️ Running the Application

### Windows
1. Open Command Prompt or PowerShell
2. Navigate to project folder:
   ```cmd
   cd path\to\python-project-bundler
   ```
3. Run:
   ```cmd
   python project_bundler.py
   ```

### Linux/macOS
1. Open Terminal
2. Navigate to project folder:
   ```bash
   cd path/to/python-project-bundler
   ```
3. Run:
   ```bash
   python3 project_bundler.py
   ```

---

## 🎯 Your First Backup

### Step 1: Choose Your Project
1. Click **"📁 Choose Project Folder"**
2. Navigate to your Python project
3. Select the folder

### Step 2: Create Archive
1. Click **"📦 Bundle → Create .txt Archive"**
2. Choose where to save (default: same folder with timestamp)
3. Click "Save"

✅ **Done!** All your `.py` files are now in one text file.

---

## 🔄 Your First Restore

### Step 1: Choose Destination
1. Click **"📁 Choose Project Folder"**
2. Select where to restore files (can be new empty folder)

### Step 2: Select Archive
1. Click **"📥 Restore ← From .txt Archive"**
2. Choose your `.txt` archive file

### Step 3: Choose Files
A dialog appears showing all files:
- **Green** = File exists (will be overwritten)
- **Orange** = New file (will be created)

Options:
- Select specific files to restore (Ctrl+Click to select multiple)
- Leave empty to restore only existing files
- Check "Ask before creating..." to confirm each new file

### Step 4: Restore
1. Click **"Continue Restoration"**
2. Wait for completion message

✅ **Done!** Your files are restored.

---

## 👀 View Archive Contents

Want to see what's in an archive without restoring?

1. Click **"📋 View .txt Archive Contents"**
2. Select archive file
3. Browse file list with status indicators

---

## 💡 Tips & Tricks

### Archive Naming
Default format: `ProjectName_YYYY-MM-DD_HH-MM.txt`

Example: `my-app_2026-02-15_14-30.txt`

### Selective Restore
To restore only specific files:
1. In the selection dialog, click files you want (Ctrl+Click for multiple)
2. Click "Continue Restoration"

### Backup Strategy
- **Daily**: Create archive at end of workday
- **Before experiments**: Archive before major changes
- **Version milestones**: Archive when reaching project milestones
- **Pre-refactor**: Archive before major code restructuring

### Archive as Documentation
The text format makes archives:
- Easy to read in any text editor
- Searchable (Ctrl+F to find code)
- Shareable via email or chat
- Version-control friendly

---

## 📁 Example Workflow

### Scenario: Sharing Project with Colleague

1. **Bundle your project:**
   ```
   Choose folder → Bundle → Save as "my-project_v1.txt"
   ```

2. **Send archive:**
   - Email the `.txt` file
   - Or share via cloud storage
   - Or send in chat

3. **Colleague restores:**
   ```
   Create new folder → Choose folder → Restore → Select your archive
   ```

✅ They now have complete project!

---

## ⚠️ Common Mistakes

### ❌ Wrong: Selecting file instead of folder
When choosing project, select the **folder**, not a file inside it.

### ❌ Wrong: Overwriting without backup
Always create a new archive before restoring over existing project.

### ✅ Correct: Archive first, then restore
```
1. Bundle current project → my-project_backup.txt
2. Restore from archive → Restore to same folder
```

---

## 🆘 Troubleshooting

### "No .py files found"
- Make sure you selected correct folder
- Check folder actually contains `.py` files
- Verify file extensions (not `.txt` or `.python`)

### "Permission denied" on restore
- Check folder write permissions
- Close files in other programs (IDEs, text editors)
- Try running as administrator (Windows)

### "Encoding error"
- Project uses UTF-8 encoding
- If files use different encoding, convert first
- Or edit `project_bundler.py` to change encoding

### Files not appearing after restore
- Check you selected correct destination folder
- Verify restoration completed (check status message)
- Look for error messages in status bar

---

## 🎓 Next Steps

Now that you're familiar with basics:

1. **Read full README**: Detailed features and options
2. **Check CONTRIBUTING**: Help improve the project
3. **Explore code**: Learn from well-documented OOP structure
4. **Star on GitHub**: Show support if you find it useful!

---

## 📞 Need Help?

- **Issues**: https://github.com/Patisons/python-project-bundler/issues
- **Discussions**: https://github.com/Patisons/python-project-bundler/discussions

---

**Happy Bundling! 🎉**
