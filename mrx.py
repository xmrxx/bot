from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8099846862:AAH9MygiDideA59LynRO3wYLix8kxpwuKjs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [
        [InlineKeyboardButton(
            "الدخول الى موقع الجامعة الاسلامية",
            web_app=WebAppInfo(url="https://mrx.zya.me/bot.html")
        )],
        [InlineKeyboardButton(
            "📍 موقع الجامعة (الخريطة)",
            url="https://maps.app.goo.gl/76GVNAUg1B4GxxJF8"
        )]
    ]
    await update.message.reply_text(
        "المجيب الالي للجامعة الاسلامية فرع الديوانية:",
        reply_markup=InlineKeyboardMarkup(kb)
    )

# استقبال البيانات العائدة من الويب-أب
async def on_webapp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if msg and msg.web_app_data:  # بيانات قادمة من tg.sendData(...)
        await msg.reply_text(f"وصلتني البيانات: {msg.web_app_data.data}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, on_webapp))  # نفحص web_app_data داخل كل رسالة
    app.run_polling()

if __name__ == "__main__":
    main()
