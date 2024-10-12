import argparse

import requests

# richライブラリのインポートを試みる
try:
    from rich.console import Console
    from rich.text import Text
except ImportError:
    Console = None  # richがインストールされていない場合はNoneに設定

# コンソールオブジェクトを作成（richがインストールされている場合のみ）
console = Console() if Console else None


def print_message(message: str, style: str = None):
    """メッセージを印刷する関数。richまたは通常のprintを使用する。"""
    if console:
        if style:
            styled_message = Text(message, style=style)
            console.print(styled_message)
        else:
            console.print(message)
    else:
        print(message)


def validate_theme_id_format(theme_id: str) -> bool:
    """Validate the format of a theme ID."""
    return len(theme_id) >= 6 and all(c.isalnum() or c == "-" for c in theme_id)


def validate_platform(platform: str) -> bool:
    """Validate platform input."""
    valid_platforms = ["ANDROID", "IOS"]
    return platform.upper() in valid_platforms


def check_http_response_status(uri: str) -> bool:
    """Check if it is able to get the URI content."""
    try:
        response = requests.get(uri)
        return response.status_code == 200
    except requests.RequestException:
        return False


def build_theme_evidence_uri(theme_id: str, version: int) -> str:
    """Returns the URI of a small asset associated with the specified theme."""
    subdir1 = theme_id[:2]
    subdir2 = theme_id[2:4]
    subdir3 = theme_id[4:6]
    base_uri = "http://dl.shop.line.naver.jp/themeshop/v1/products"
    pack_uri = f"{base_uri}/{subdir1}/{subdir2}/{subdir3}/{theme_id}"
    return f"{pack_uri}/{version}/ANDROID/icon_86x123.png"


def build_theme_zip_uri(theme_id: str, version: int, platform: str) -> str:
    """Returns the URI of the specified theme's zip."""
    subdir1 = theme_id[:2]
    subdir2 = theme_id[2:4]
    subdir3 = theme_id[4:6]
    base_uri = "http://dl.shop.line.naver.jp/themeshop/v1/products"
    pack_uri = f"{base_uri}/{subdir1}/{subdir2}/{subdir3}/{theme_id}"
    return f"{pack_uri}/{version}/{platform}/theme.zip"


def check_theme_existence(theme_id: str, version: int = 1) -> bool:
    """Check if the URI content exists as evidence of the theme's existence."""
    return check_http_response_status(build_theme_evidence_uri(theme_id, version))


def build_theme_zip_filename(theme_id: str, version: int, platform: str) -> str:
    """Returns a filename to save a theme zip."""
    return f"Theme-{theme_id}-{version}-{platform}.zip"


def download_theme_zip(theme_id: str, version: int, platform: str) -> str:
    """Download the zip of the specified theme and return the path where it's saved."""
    uri = build_theme_zip_uri(theme_id, version, platform)
    path = build_theme_zip_filename(theme_id, version, platform)

    # ダウンロード中のメッセージを表示
    print_message(
        f"📥 Downloading: {theme_id} (version {version}, platform {platform})"
    )

    response = requests.get(uri)
    with open(path, "wb") as f:
        f.write(response.content)

    # ダウンロード成功後のメッセージに置き換え
    print_message(f"✅ Saved: {path} ({platform})")
    return path


def check_theme_details(theme_id: str):
    """指定されたテーマIDの詳細を表示します。"""
    available_versions = []
    for i in range(1, 100):  # 100は任意の上限; 必要に応じて調整
        if check_theme_existence(theme_id, i):
            available_versions.append(i)
        else:
            break

    if available_versions:
        print_message(
            f"✅ Available versions for {theme_id}: {', '.join(map(str, available_versions))}",
            style="green",
        )
    else:
        print_message(f"❌ No available versions for {theme_id}", style="red")


def main():
    # Command-line arguments
    parser = argparse.ArgumentParser(
        description="Downloads theme packages based on the provided ID, version, and platform."
    )
    parser.add_argument(
        "--id", type=str, required=True, help="The theme ID to be downloaded."
    )
    parser.add_argument(
        "--version",
        type=int,
        default=0,  # デフォルトで最新バージョンを指定
        help="The version of the theme to be downloaded. Use -1 for all versions, 0 for the latest version.",
    )
    parser.add_argument(
        "--platform",
        type=str,
        nargs="?",  # 引数があれば一つ、なければ全てのプラットフォームを対象
        const="BOTH",  # 引数なしの場合に指定
        default="BOTH",  # デフォルトは両方のプラットフォーム
        help="The platform to download for, either 'ANDROID', 'IOS', or leave empty for both.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check available versions for the specified theme ID.",
    )

    args = parser.parse_args()

    # Verify the command-line arguments
    if args.version < -1:
        raise ValueError("Package version parameter out of range")
    if not validate_theme_id_format(args.id):
        raise ValueError("Invalid package ID format")
    if args.platform != "BOTH" and not validate_platform(args.platform):
        raise ValueError(
            "Invalid platform specified. Use 'ANDROID', 'IOS', or leave empty for both."
        )

    if args.check:
        check_theme_details(args.id)
        return  # --checkオプションの場合はここで終了

    # Check if the specified theme exists
    if args.version < 1:
        if not check_theme_existence(args.id):
            raise ValueError("No such theme package (possibly network error)")
        print_message(f"✅ Verified: {args.id}", style="green")
    else:
        if not check_theme_existence(args.id, args.version):
            raise ValueError(
                "No such theme package or specified version (possibly network error)"
            )
        print_message(f"✅ Verified: {args.id} (version {args.version})", style="green")

    # Downloading process
    platforms = ["ANDROID", "IOS"] if args.platform == "BOTH" else [args.platform]

    for platform in platforms:
        skipped_versions = []  # スキップしたバージョンを格納するリスト
        latest_version = None  # ダウンロードしたバージョンを保持する変数

        if args.version == -1:
            # Download all versions
            for i in range(1, 100):  # 100 is arbitrary; adjust as needed
                if not check_theme_existence(args.id, i):
                    break
                latest_version = i  # 最新バージョンを更新
                # ダウンロード処理を呼び出す
                download_theme_zip(args.id, latest_version, platform)
        elif args.version == 0:
            # Download the latest version
            for i in range(1, 100):  # 100 is arbitrary; adjust as needed
                if not check_theme_existence(args.id, i):
                    break
                if latest_version is not None:
                    skipped_versions.append(
                        latest_version
                    )  # 最新バージョンをスキップリストに追加
                latest_version = i  # 最新バージョンを更新
            if skipped_versions:
                print_message(
                    f"⏭️ Skipped versions for {args.id} on platform {platform}: {', '.join(map(str, skipped_versions))}"
                )
            if latest_version:
                # ダウンロード処理を呼び出す
                download_theme_zip(args.id, latest_version, platform)
        else:
            # Download the specified version
            download_theme_zip(args.id, args.version, platform)


if __name__ == "__main__":
    main()
