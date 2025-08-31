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

bot.polling()

