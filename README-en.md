---

# Nezu Theme Downloader

## Japanese: [ja-JP](README.md)

The Nezu Theme Downloader provides a script for downloading specified theme packages:

- **Python Script**: `downloader.py`

This script downloads themes based on a specified theme ID, version, and platform (Android or iOS). If no version is specified, the latest version is downloaded by default.

---

## 📂 Structure

```
/theme_downloader
├── downloader.py      # Python script
└── README-en.md               # This README file
```

---

## 1. Overview

### 🎯 Purpose of the Theme Downloader

- **Goal**: To allow users to download a specified theme for a given platform.
- **Supported Platforms**: Android and iOS.
- **Download Target**: Theme ZIP files based on theme ID and version. If no version is specified, the latest version is downloaded by default.

---

## 2. Python Script (`downloader.py`)

### 📜 Overview

This script runs in a Python environment and downloads the ZIP file of the specified theme.

### 🛠️ Usage

#### 🔧 Arguments

- `--id <theme_id>`: The ID of the theme to be downloaded.
- `--version <version>`: The version of the theme to be downloaded. `-1` specifies all versions, while `0` specifies the latest version. If not specified, the latest version is downloaded by default.
- `--platform <platform>`: The platform for downloading (either `ANDROID` or `IOS`). The default is `BOTH` (both platforms).
- `--check`: Check available versions for the specified theme ID and output the details.

#### ⚙️ Execution Steps

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is saved. For example:
   ```bash
   cd /path/to/directory
   ```
3. Execute the script from the command line.

### 💡 Examples:

- Download the latest version for the Android platform:
  ```bash
  python downloader.py --id bfdcaa2e-fe09-4178-bfd9-16295fbb8376 --platform ANDROID
  ```

- Check available versions for the theme ID:
  ```bash
  python downloader.py --id bfdcaa2e-fe09-4178-bfd9-16295fbb8376 --check
  ```

---

## 📜 Output Format

- **Use of Rich Library**: The script provides beautiful output when the `rich` library is installed. If `rich` is not available, it falls back to standard `print`.

- **Download Messages**: When the download starts, a message saying "📥 Downloading: ..." is displayed, and upon successful download, it changes to "✅ Saved: ...".

---

## ⚠️ Important Notes

1. **Request from LINE**: 
   If a formal request is made from LINE, this repository will be removed immediately.

2. **Compliance with Laws**:
   Ensure compliance with all applicable laws, regulations, and license terms when using this tool. Unauthorized use or infringement of copyright is strictly prohibited.

3. **For Personal Use Only**:
   This tool is intended for personal use only. Commercial use or redistribution is not permitted.

Users are expected to use the tool in agreement with these conditions. If these conditions are violated, cease the use of the tool immediately.

---

## 📝 License

This project is licensed under the **MIT License**.

---