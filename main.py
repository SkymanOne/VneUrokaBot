import telebot
from telebot import types
from models_pack import db_access, constants
from token_const import token
from MyLogs import *

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda message: message.text == 'Главное меню✅')
def main_start(message: types.Message):
    my_log_info(message.from_user, 'начата работа с ботом, нажата кнопка /start или Гавное меню')
    markup = types.ReplyKeyboardMarkup()
    markup.row('Доступные игры📲', 'Лидеры по играм⚜️')
    markup.row('Справка🌚')
    my_log_info(message.from_user, 'отрисовка главного меню')
    bot.send_message(message.from_user.id, 'Приветствую тебя, ' + message.from_user.first_name
                     + ', что желаешь?', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Доступные игры📲')
def aviable_games(message: types.Message):
    my_log_info(message.from_user, 'нажата кнопка "Доступные книги"')
    markup = types.ReplyKeyboardMarkup()
    markup.row('Квест🚸', 'Главное меню✅')
    bot.send_message(message.from_user.id, 'Вот тебе список доступных игр:',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Квест🚸')
def game(message: types.Message):
    my_log_info(message.from_user, 'Нажата кнопка Квест')
    markup = types.ReplyKeyboardMarkup()
    markup.row('Начать игру⛳️', 'Рейтинг📊')
    markup.row('Доступные игры📲', 'Главное меню✅')
    bot.send_message(message.from_user.id, 'Типо описание игры',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Начать игру⛳️')
def start_game(message: types.Message):
    my_log_info(message.from_user, 'начала игру')
    user = db_access.get_user(message.from_user.id)
    my_log_info(message.from_user, 'поиск пользователя в бд')
    if user is None:
        my_log_info(message.from_user, 'Пользователь не найден')
        db_access.create_user(message.from_user, datetime.now())
        my_log_info(message.from_user, 'Регистрация пользователя в бд')
        bot.send_message(message.from_user.id, 'Ты в игре')
    else:
        my_log_info(message.from_user, 'найден в бд')
        bot.send_message(message.from_user.id, 'Ты уже в игре ' + user.user_name)
        level = db_access.get_level(message.from_user.id)
        bot.send_message(message.from_user.id, 'Твой уровень: ' + str(level))


bot.polling(True)
