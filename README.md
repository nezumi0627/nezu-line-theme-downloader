以下の内容から、PowerShell スクリプトに関連する部分を削除したバージョンを作成しました。

---

# Nezu Theme Downloader

## English: [en-US](README.md)

Nezu Theme Downloaderでは、指定されたテーマパッケージをダウンロードするためのスクリプトを提供しています：

- **Python スクリプト**: `downloader.py`

このスクリプトは、特定のテーマ ID、バージョン、およびプラットフォーム（Android または iOS）に基づいてテーマをダウンロードします。バージョンが指定されていない場合は、最新バージョンがデフォルトでダウンロードされます。

---

## 📂 構造

```
/theme_downloader
├── downloader.py      # Python スクリプト
└── README.md              # この README ファイル
```

---

## 1. 概要

### 🎯 テーマダウンローダーの目的

- **目的**: ユーザーが指定したテーマを、指定されたプラットフォーム向けにダウンロードすること。
- **対応プラットフォーム**: Android および iOS。
- **ダウンロードの対象**: テーマ ID とバージョンに基づくテーマ ZIP ファイル。バージョンが指定されていない場合は、最新バージョンがデフォルトでダウンロードされます。

---

## 2. Python スクリプト (`downloader.py`)

### 📜 概要

このスクリプトは、Python 環境で実行され、指定されたテーマの ZIP ファイルをダウンロードします。

### 🛠️ 使用方法

#### 🔧 引数

- `--id <theme_id>`: ダウンロードするテーマの ID。
- `--version <version>`: ダウンロードするテーマのバージョン。`-1` はすべてのバージョン、`0` は最新バージョンを指定します。指定がない場合は、最新バージョンがデフォルトでダウンロードされます。
- `--platform <platform>`: ダウンロード対象のプラットフォーム（`ANDROID` または `IOS`）。デフォルトは `BOTH`（両方のプラットフォーム）。
- `--check`: 指定されたテーマ ID に対する利用可能なバージョンを確認し、詳細を出力します。

#### ⚙️ 実行手順

1. ターミナルまたはコマンドプロンプトを開きます。
2. スクリプトが保存されているディレクトリに移動します。例えば:
   ```bash
   cd /path/to/directory
   ```
3. コマンドラインより、スクリプトを実行します。

### 💡 例:

- 最新バージョンを Android プラットフォーム向けにダウンロードする
  ```bash
  python downloader.py --id bfdcaa2e-fe09-4178-bfd9-16295fbb8376 --platform ANDROID
  ```

- テーマ ID の利用可能なバージョンを確認する
  ```bash
  python downloader.py --id bfdcaa2e-fe09-4178-bfd9-16295fbb8376 --check
  ```

---

## 📜 出力形式

- **rich ライブラリの利用**: スクリプトは、`rich` ライブラリがインストールされている場合に美しい出力を提供します。`rich` がない場合は、通常の `print` にフォールバックします。

- **ダウンロードメッセージ**: ダウンロードが開始されると、「📥 Downloading: ...」というメッセージが表示され、ダウンロード成功後に「✅ Saved: ...」というメッセージに置き換わります。

---

## ⚠️ 重要な注意事項

1. **LINEからの要請**: 
   LINEからの正式な要請があった場合、このリポジトリは直ちに削除されます。

2. **法令遵守**:
   本ツールの使用にあたっては、必ず適用される全ての法律、規制、およびライセンス条項を遵守してください。違法行為や著作権侵害を目的とした使用は固く禁じられています。

3. **個人使用のみ**:
   このツールは個人的な使用のみを目的としています。商業目的での使用や再配布は許可されていません。

ユーザーは、これらの条件に同意した上でツールを使用するものとします。これらの条件に違反した場合、ツールの使用を直ちに中止してください。

---

## 📝 ライセンス

このプロジェクトは **MIT ライセンス** の下で提供されています。

---