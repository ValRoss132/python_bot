import telebot
from telebot import types

bot = telebot.TeleBot("5567703954:AAEHnu39wtvRCLmXGiVEPkREumhl70yEhUc")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton("audio")
    photo = types.KeyboardButton('photo')
    markup.add(website, photo)  
    mes = f"Привет, {message.from_user.first_name} {message.from_user.last_name}"
    bot.send_message(message.chat.id, mes, reply_markup=markup)

@bot.message_handler(commands=['website'])
def web(message):
    markup = types.InlineKeyboardMarkup()  
    markup.add(types.InlineKeyboardButton('Кликни сюда:', url="https://vk.com/cf0712"))           
    bot.send_message(message.chat.id, "Туда-сюда", reply_markup=markup)

@bot.message_handler(commands=['help'])
def web(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton("/website")
    start = types.KeyboardButton('/start')
    markup.add(website, start)        
    bot.send_message(message.chat.id, "Туда-сюда", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "help":
        bot.send_message(message.chat.id, message)
    elif message.text == "Привет":
        bot.send_message(message.chat.id, "привет привет")
    elif message.text == "Пока":
        bot.send_message(message.chat.id, "ПОКА, тварь")
    elif message.text == "photo":
        ph = open('1.jpg', 'rb')
        bot.send_photo(message.chat.id, ph)
    elif message.text == "audio":
        audio = open('123.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    else:
        bot.send_message(message.chat.id, "Ты тупой? Я тебя не понимаю")

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Круто!")







bot.polling(none_stop=True)