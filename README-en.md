# Nezu Theme Downloader

## English: [ja-JP](README.md)

The Nezu Theme Downloader provides a script to download specified theme packages:

- **Python Script**: `downloader.py`

This script downloads themes based on a specific theme ID, version, and platform (Android or iOS). If no version is specified, the latest version will be downloaded by default.

---

## 📂 Structure

```
/theme_downloader
├── downloader.py      # Python script
└── README.md          # This README file
```

---

## 1. Overview

### 🎯 Purpose of the Theme Downloader

- **Objective**: To download the theme specified by the user for the specified platform.
- **Supported Platforms**: Android and iOS.
- **Download Target**: Theme ZIP files based on theme ID and version. If no version is specified, the latest version will be downloaded by default.

---

## 2. Python Script (`downloader.py`)

### 📜 Overview

This script runs in a Python environment and downloads the ZIP file of the specified theme.

### 🛠️ How to Use

#### 🔧 Arguments

- `--id <theme_id>`: The ID of the theme to download.
- `--version <version>`: The version of the theme to download. `-1` specifies all versions, and `0` specifies the latest version. If not specified, the latest version will be downloaded by default.
- `--platform <platform>`: The platform to download for (`ANDROID` or `IOS`). The default is `BOTH` (both platforms).
- `--check`: Checks the available versions for the specified theme ID and outputs the details.

#### ⚙️ Execution Steps

1. Open the terminal or command prompt.
2. Navigate to the directory where the script is saved. For example:
   ```bash
   cd /path/to/directory
   ```
3. Execute the script from the command line.

### 💡 Example:

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

- **Using the `rich` Library**: The script provides beautiful output if the `rich` library is installed. If `rich` is not available, it falls back to the regular `print`.

- **Download Messages**: When the download starts, a message "📥 Downloading: ..." is displayed, which is displayed as "✅ Saved: ..." after a successful download.

If you need any further changes or assistance, just let me know!
---

## ⚠️ Important Notes

1. **Requests from LINE**: 
   If there is an official request from LINE, this repository will be deleted immediately.

2. **Compliance with Laws**:
   When using this tool, please comply with all applicable laws, regulations, and licensing terms. Usage for illegal activities or copyright infringement is strictly prohibited.

3. **For Personal Use Only**:
   This tool is intended for personal use only. Commercial use or redistribution is not allowed.

Users are expected to use the tool in agreement with these conditions. If you violate these conditions, please cease using the tool immediately.

---

## 📝 License

This project is provided under the **MIT License**.

--- 