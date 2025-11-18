import telebot
import os
from openai import OpenAI

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Перевірка токенів
if TELEGRAM_TOKEN is None:
    raise ValueError("TELEGRAM_TOKEN не встановлено!")
if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY не встановлено!")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привіт! Я AI-бот. Пиши будь-що — я відповім!")

@bot.message_handler(func=lambda msg: True)
def chat(message):
    user_text = message.text

    # ❗ НОВИЙ синтаксис OpenAI
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Ти дружній помічник."},
            {"role": "user", "content": user_text}
        ]
    )

    # ❗ Правильний доступ до контенту (новий формат)
    answer = completion.choices[0].message["content"]

    bot.reply_to(message, answer)

bot.polling(none_stop=True)