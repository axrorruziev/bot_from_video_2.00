from telebot import types

def button_main():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('uz')
    btn2 = types.KeyboardButton('ru')
    buttons.add(btn1, btn2)
    return buttons
