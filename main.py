import telebot
import os
from openai import OpenAI

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привіт! Я AI-бот. Пиши будь-що — я відповім!")

@bot.message_handler(func=lambda msg: True)
def chat(message):
    user_text = message.text

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_text}]
    )

    answer = response.choices[0].message["content"]
    bot.reply_to(message, answer)

bot.polling()