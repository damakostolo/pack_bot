import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot('5971340761:AAFCF7-chA51k0Mq-AdgjEjIfoZ4bYYAZNE')


# Начало работы создаём кнопки и отпровляем фото
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Мама я панк!")
    markup.row(btn1)

    btn2 = types.KeyboardButton("Удалить фото")
    btn3 = types.KeyboardButton("изменмть текст")
    markup.row(btn2, btn3)
   
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == "Мама я панк!":
        bot.send_message(message.chat.id, "Переход на сайт")
    elif message.text == "Удалить фото":
        bot.send_message(message.chat.id, "delet")


@bot.message_handler(content_types=['photo'])  # создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(
        "Мама я панк!", url='https://youtu.be/dQw4w9WgXcQ')
    markup.row(btn1)

    btn2 = types.InlineKeyboardButton("Удалить фото", callback_data='delete')
    btn3 = types.InlineKeyboardButton("изменмть текст", callback_data='edit')
    markup.row(btn2, btn3)

    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(
        message.from_user), reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id,
                           callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text(
            'edit text', callback.message.chat.id, callback.message.message_id)


bot.polling(non_stop=True)
