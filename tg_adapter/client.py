from telegram import Bot

bot = Bot(token="YOUR_BOT_TOKEN")

def send_to_telegram(chat_id, text):
    bot.send_message(chat_id=chat_id, text=text)