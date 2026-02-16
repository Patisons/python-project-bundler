# Python Project Bundler & Restorer

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: DWTFYW](https://img.shields.io/badge/License-Do%20What%20You%20Want-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](https://github.com/yourusername/python-project-bundler)

A simple, GUI-based tool for backing up and restoring Python projects by bundling all `.py` files into a single text archive.

**🌍 Languages:** [English](#) | [Русский](docs/README_RU.md) | [Latviešu](docs/README_LV.md)

---

## 📋 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Requirements](#-requirements)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- **📦 Bundle Projects**: Combine all Python files in a folder into a single `.txt` archive
- **📥 Restore Projects**: Extract and restore files from archive back to project folder
- **🎯 Selective Restoration**: Choose which files to restore via visual interface
- **🔍 Archive Preview**: View archive contents without restoring
- **🎨 User-Friendly GUI**: Clean, modern Tkinter interface
- **🛡️ Safe Operations**: Color-coded warnings for existing files
- **⚙️ Flexible**: Choose both project folder and archive save location

---

## 📸 Screenshots

### Main Window
![Main Window](docs/images/main_window.png)
*The main interface with three primary actions*

### File Selection Dialog
![File Selection](docs/images/file_selection.png)
*Choose which files to restore with color-coded status*

---

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- tkinter (usually included with Python)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Patisons/python-project-bundler.git
   cd python-project-bundler
   ```

2. **Run the application:**
   ```bash
   python project_bundler.py
   ```

That's it! No external dependencies required.

---

## 📖 Usage

### 1. Bundling Files (Creating Archive)

1. Click **"Choose Project Folder"** and select your Python project directory
2. Click **"📦 Bundle → Create .txt Archive"**
3. Choose where to save the archive (default: project folder with timestamp)
4. Done! All `.py` files are now bundled into a single text file

### 2. Restoring Files (From Archive)

1. Click **"Choose Project Folder"** to select destination folder
2. Click **"📥 Restore ← From .txt Archive"**
3. Select the archive file to restore from
4. In the selection dialog:
   - **Green** files = already exist (will be overwritten)
   - **Orange** files = don't exist (will be created)
5. Select files to restore (or select none to restore all existing files)
6. Optionally check "Ask before creating non-existing files"
7. Click **"Continue Restoration"**

### 3. Viewing Archive Contents

1. Click **"📋 View .txt Archive Contents"**
2. Select an archive file
3. View all files stored in the archive without restoring them

---

## 🔧 How It Works

### Archive Format

The tool creates human-readable text archives with this structure:

```
# Project Archive – MyProject
# Date: 2026-02-15 12:30:45
# Total files: 3

=== main.py ===
import tkinter as tk
...
=== END ===

=== utils.py ===
def helper():
    ...
=== END ===

=== config.py ===
settings = {}
...
=== END ===
```

### Key Components

- **ProjectManager**: Handles file operations in the project directory
- **ArchiveManager**: Creates and parses text archives
- **FileSelectionDialog**: Interactive file selection for restoration
- **ProjectBundlerApp**: Main GUI application

---

## 📦 Requirements

- **Python**: 3.7+
- **Built-in modules only**:
  - `tkinter` - GUI framework
  - `pathlib` - File path operations
  - `datetime` - Timestamps
  - `re` - Archive parsing

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Improvement

- Add support for other file types (`.txt`, `.md`, `.json`, etc.)
- Implement compression for large projects
- Add project templates
- Create CLI version
- Add archive encryption option

---

## 📄 License

**Do What You Want License** - Use it however you want. No restrictions. No conditions. Just don't blame me if something breaks! 😄

See the [LICENSE](LICENSE) file for the full "legal mumbo-jumbo" (spoiler: it's very short and human-readable).

**Want to say thanks?** Check the LICENSE file for optional ways to support the project.

---

## 👨‍💼 Author

Created with ❤️ by **Pats-MK** and **Claude**

---

## 🙏 Acknowledgments

- Built using Python's standard library only
- Inspired by the need for simple, portable project backups
- Thanks to the Python community for excellent documentation

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Patisons/python-project-bundler/issues) page
2. Create a new issue with:
   - Your Python version
   - Operating system
   - Steps to reproduce the problem
   - Error messages (if any)

---

**⭐ If you find this tool useful, please consider giving it a star!**
