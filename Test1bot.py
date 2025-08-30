from random import randint
import telebot
from telebot import types
from config import test1_bot

TOKEN = test1_bot
bot = telebot.TeleBot(TOKEN)

game = False
restart = False
num = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("YES!!!")
    btn2 = types.KeyboardButton("NONONO:(((((")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Hi!!! Do you want to start a guess-game?", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global game, num, restart
    text = message.text.lower()

    if text == "yes!!!":
        bot.reply_to(message, "Sooooo, let's start!")
        game = True
        num = randint(1, 10)
        return

    elif text == "nonono:(((((":
        bot.reply_to(message, "Bye! T-T")
        game = False
        return

    if game:
        try:
            gues = int(text)
            if gues < num:
                ans = "My number is greater!"
            elif gues > num:
                ans = "My number is less!"
            else:
                ans = "You've guessed it!"
                game = False
                restart = True
            bot.reply_to(message, ans)
        except:
            bot.send_message(message.chat.id, "Please, send a number!")

    if restart:
        restart = False
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("YES!!!")
        btn2 = types.KeyboardButton("NONONO:(((((")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Do you want to repeat?", reply_markup=markup)

bot.polling()
