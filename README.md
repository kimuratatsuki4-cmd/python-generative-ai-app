# 🤖 AI Chat Application

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?style=flat-square&logo=flask)
![Google GenAI](https://img.shields.io/badge/Google%20GenAI-API-red?style=flat-square&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

⚠️ **重要: このアプリケーションは Google GenAI API の無料枠を利用しています**

## 📋 概要

Google GenAI（Gemini）を活用したチャットアプリケーションです。Flask で構築されており、シンプルで直感的なUIでAIとの会話ができます。

## ✨ 機能

- 💬 リアルタイム AI チャット
- 🎨 モダンでレスポンシブなデザイン
- 🔒 セキュアな環境変数管理
- ⚡ 高速なレスポンス処理
- 🛡️ XSS対策（HTMLエスケープ）

## 🛠️ 使用技術

| 技術 | バージョン | 用途 |
|------|-----------|------|
| Python | 3.13 | プログラミング言語 |
| Flask | 3.1.3 | Webフレームワーク |
| Google GenAI | 1.73.1 | AI API |
| Jinja2 | 3.1.6 | テンプレートエンジン |
| Python-dotenv | - | 環境変数管理 |

## 📋 前提条件

- Python 3.13 以上
- pip (Python パッケージマネージャー)
- Google GenAI API キー

## 🚀 インストール

### 1. リポジトリをクローン
```bash
cd python-generative-ai-app
```

### 2. 仮想環境を作成・有効化
```bash
# Windows
python -m venv flask_env
.\flask_env\Scripts\activate

# macOS/Linux
python3 -m venv flask_env
source flask_env/bin/activate
```

### 3. 依存パッケージをインストール
```bash
pip install -r requirements.txt
```

### 4. 環境変数を設定

`.env` ファイルをプロジェクトルートに作成します：

```env
GOOGLE_API_KEY=your_api_key_here
FLASK_ENV=development
```

**Google API キーの取得方法:**
1. [Google AI Studio](https://aistudio.google.com/app/apikeys) にアクセス
2. 「Get API Key」をクリック
3. 「Create API key in new project」を選択
4. 生成されたキーを `.env` ファイルに貼り付け

⚠️ **.env ファイルを絶対に Git にコミットしないでください！**

## 🎯 使用方法

### 開発サーバー起動
```bash
# 仮想環境を有効化（初回のみ）
.\flask_env\Scripts\activate  # Windows
source flask_env/bin/activate  # macOS/Linux

# Flask アプリケーション起動
python app.py
```

### ブラウザアクセス
```
http://localhost:5000
```

## 📁 プロジェクト構成

```
python-generative-ai-app/
├── app.py                 # メインアプリケーション
├── .env                   # 環境変数（.gitignore対象）
├── .gitignore             # Git除外ファイル
├── requirements.txt       # 依存パッケージ一覧
├── README.md              # このファイル
├── templates/
│   └── index.html         # HTMLテンプレート
├── static/
│   └── css/
│       └── style.css      # CSSスタイルシート
└── flask_env/             # 仮想環境（バージョン管理外）
```

## 💡 使用例

1. メッセージ入力欄に質問を入力
2. 「質問する」ボタンをクリック
3. AI が回答を生成して表示

### 例:
**ユーザー:** 「Pythonについて教えてください」  
**AI:** 「Pythonはシンプルで読みやすい高水準プログラミング言語です...」

## ⚠️ 無料 API 利用に関する注意事項

このアプリケーションは **Google GenAI の無料枠** を利用しています：

| 制限事項 | 詳細 |
|---------|------|
| **Rate Limit** | 15 リクエスト/分 |
| **エラーコード 429** | レート制限に達した場合 |
| **制限解除方法** | 1分待機後に再試行 |

詳細は [Google GenAI API 料金ページ](https://ai.google.dev/pricing) を参照してください。

## 🔒 セキュリティ機能

- ✅ APIキーの環境変数管理
- ✅ HTML エスケープによる XSS 対策
- ✅ エラーメッセージの安全な表示
- ✅ .env ファイルの Git 管理外

## 🐛 トラブルシューティング

### エラー: `GOOGLE_API_KEY が .env ファイルに設定されていません`
**解決方法:** `.env` ファイルが存在し、`GOOGLE_API_KEY` が正しく設定されているか確認してください。

### エラー: `ModuleNotFoundError: No module named 'dotenv'`
**解決方法:** 以下を実行してください
```bash
pip install python-dotenv
```

### レスポンスが遅い
**原因:** Google API のレート制限に達している可能性があります  
**解決方法:** 1分待機してから再度お試しください

## 📚 参考リソース

- [Flask 公式ドキュメント](https://flask.palletsprojects.com/)
- [Google GenAI Python SDK](https://github.com/googleapis/python-genai)
- [Google Gemini API ドキュメント](https://ai.google.dev/docs)

## 📄 ライセンス

MIT License - 詳細は [LICENSE](LICENSE) ファイルを参照

## 👤 作成者

Python AI Chat Application

---

**最終更新:** 2026年4月21日  
**Python バージョン:** 3.13  
**Flask バージョン:** 3.1.3
