from random import choice
import telebot
from telebot import types
from config import test1_bot

TOKEN = test1_bot
TOKEN = "8417248785:AAGvqPg_pPMdsa0Ncb-CrPhDa4dbi0qC8nk"
bot = telebot.TeleBot(TOKEN)

class Car():
    def __init__(self, brand:str, color:str):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"{self.brand}, {self.color}"

variants = ["OREL", "RESHKA"]
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("/coin")
    markup.add(btn1)
    bot.reply_to(message, "Hi!!! Use cmd 'coin' to flip it! Additionally, you can use '/car brand color' to make new obj", reply_markup = markup)

@bot.message_handler(commands=['coin'])
def coin(message):
    bot.send_message(message.chat.id, choice(variants))

@bot.message_handler(commands=['car'])
def car(message):
    global variants
    info = telebot.util.extract_arguments(message.text)
    car = Car(*info.split())
    bot.send_message(message.chat.id, f"Your new obj is: '{car}'")
    variants.append(car)

banned_users = {}

@bot.message_handler(commands=['ban'])
def ban(message):
    if message.reply_to_message: #message.reply_to_message.text
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.username
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:

            if not user_id in banned_users.keys():
                banned_users[user_id] = user_name
                bot.reply_to(message, "LAST WARNING! if you sent ban word again, you will be banned!")
            else:
                # bot.ban_chat_member(chat_id, user_id)
                bot.send_message(message.chat.id, "BANBANBAN")

@bot.message_handler(commands=['banned_users'])
def sent_banned_users(message):
    bot.reply_to(message, *list(banned_users.values()))

ban_words = ["https://", "ban"]
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    for w in ban_words:
        if w in message.text:
            sent_rep = bot.reply_to(message, "BAN")
            ban(sent_rep)

bot.polling()
