import os
import html
from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

app = Flask(__name__)

# --- 設定 ---
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY が .env ファイルに設定されていません")
client = genai.Client(api_key=API_KEY)

@app.route("/", methods = ["GET","POST"])
def index():
    # ユーザーからのメッセージを受け取る（GETリクエスト想定）
    user_message =""
    ai_response = ""
    old_message = ""
    
    if request.method == "POST":
        user_message = request.form.get("user_message", "")
        # 初期値を上書き
        old_message = html.escape(user_message)
        
        if user_message:
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    config={
                        # 役割
                        "system_instruction": user_message,
                        "max_output_tokens": 500,
                    },
                    # message内容を指定
                    contents=user_message
                )
                ai_response = html.escape(response.text or "回答を取得できませんでした")
                
            except Exception as e:
                if "429" in str(e):
                    ai_response = "現在混み合っています。1分ほど時間を空けてから再度お試しください。"
                else:
                    ai_response = f"AI通信エラーが発生しました: {html.escape(str(e))}"

# テンプレートを取得する
    return render_template(
        "index.html",
        user_message=user_message,
        ai_response=ai_response,
        old_message=old_message
    )
    

if __name__ == "__main__":
    app.run(debug=True)