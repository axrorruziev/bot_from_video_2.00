import telebot
from telebot import types
import buttons
bot = telebot.TeleBot('6489643396:AAFzJUDrMfdqskQFD3tF4PcsJ4DuRRe4EiU')


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id,f'привет {message.from_user.first_name},выберите язык\nSalom {message.from_user.first_name},Tilin yanglang', reply_markup=buttons.button_main())
    bot.register_next_step_handler(message, uz_ru)


def uz_ru(message):
    if message.text == 'uz':
        bot.register_next_step_handler(message, uz_language)
    elif message.text == 'ru':
        bot.register_next_step_handler(message, ru_language)


def uz_language(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('YOUTUBE', url='https//youtube.com'))
    markup.add(types.InlineKeyboardButton('GOOGLE', url='https//google.com'))
    bot.send_message(message, 'qaysi saytni ochmjqchisiz??', reply_markup=markup)


def ru_language(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('YOUTUBE', url='https//youtube.com'))
    markup.add(types.InlineKeyboardButton('GOOGLE', url='https//google.com'))
    bot.send_message(message, 'какой сайт хотите открыть ?', reply_markup=markup)


bot.infinity_polling()