import telebot
import os

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = os.getenv("BOT_TOKEN") or "7508512512:AAHOuu8klbbKR6AL-5Q4qgD_bBmHHLPZLNI"

bot = telebot.TeleBot(BOT_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Добро пожаловать! Ваш chat_id: {chat_id}")

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Вы написали: {message.text}. Ваш chat_id: {chat_id}")

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
