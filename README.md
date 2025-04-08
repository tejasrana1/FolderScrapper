# 📁 File Organizer

A simple Python script that organizes files in a specified folder based on their extensions using a configurable JSON mapping.

---

## ✨ Features

- Organize files into subfolders like `Images`, `Videos`, `Docs`, etc.
- Custom extension-to-folder mapping using `config.json`
- Automatically creates folders if they don't exist
- Easy to use via command line

---

## 🧠 How It Works

1. You provide a target folder (or use the default).
2. The script reads your `config.json` file to match file extensions with folder names.
3. It moves each file to its respective folder accordingly.

---

## 📦 Installation

Make sure you have **Python 3.6+** installed.

Clone the repo:
```bash
git clone https://github.com/your-username/file-organizer.git
cd file-organizer
```bash

---

## ⚙️ Arguments

| Argument      | Description                                   | Type   | Default         |
|---------------|-----------------------------------------------|--------|-----------------|
| `-f`, `--folder` | Target folder path to organize                | `str`  | `T:/Downloads`  |
| `-c`, `--config` | Path to the config JSON file                  | `str`  | `config.json`   |

---

## 🆘 Help Command

To see all available arguments and usage:


python organizer.py --help