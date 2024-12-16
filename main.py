from create_bot import bot
import handlers.main_handler
import handlers.start_handler
import handlers.create_bot.add_bot
import os

import telebot
import os
from flask import Flask, request

ADMIN_ID = token=os.environ.get('ADMIN_ID')

# Инициализация Flask-приложения
app = Flask(__name__)




# Маршрут для Webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200

# Проверочный маршрут (опционально)
@app.route('/', methods=['GET'])
def home():
    return "Бот работает!", 200


if __name__ == "__main__":
    # Настройка Webhook при запуске сервера
    WEBHOOK_URL = f"x-hunter-bot-git-main-vladislavs-projects-a7fa5156.vercel.app/webhook"
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
