import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot('5971340761:AAFCF7-chA51k0Mq-AdgjEjIfoZ4bYYAZNE')


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)

    btn1 = types.KeyboardButton('Как я работаю' )
    btn2 = types.KeyboardButton('Стоимость роботы')
    btn3 = types.KeyboardButton('Отзывы')
    btn4 = types.KeyboardButton('Заказать работу')

    markup.add(btn1 , btn2 , btn3 , btn4)
    
    bot.send_message(message.chat.id , 'Привет , {0.first_name} , выбери пункт который тебя интересует :)'.format(message.from_user) , reply_markup= markup  )

@bot.message_handler(content_types = ['text'])
def main(message):
    if message.chat.type == 'private':
        if message.text == ('Стоимость роботы'):
            bot.send_message(message.chat.id, f"Любая работа рассмотриваеться от 100uah , дальше цена договорная.\n\nА так же веду классрумы от 100$/месяц." )

        elif message.text== ('Отзывы'):

            markup = types.InlineKeyboardMarkup(row_width= 1)
            btn1 = types.InlineKeyboardButton(
            "Чат с отзывами", url='https://t.me/+C0iOcn1q76QyNmYy')
            markup.row(btn1)

            bot.send_message(message.chat.id, "Отзывы ", reply_markup=markup)

        elif message.text== ('Как я работаю'):

            bot.send_message(message.chat.id,f"1.Работаю по предоплате 50%\n2.Все правки и переделывание работы бесплатно\n3.Дедлайны выставляете вы\n4.Работаю так же в выходные , каникулы и подобное" )

        elif message.text== ('Заказать работу'):
            
            markup = types.InlineKeyboardMarkup(row_width= 1)
            btn1 = types.InlineKeyboardButton(
            "Примеры оформления работ", url='https://t.me/+fSWsTWLiXJc5YWQy')
            markup.row(btn1)

            btn2 = types.InlineKeyboardButton(
            "Написать мне", url='https://t.me/DamaKostolol')
            markup.row(btn2)
            
            bot.send_message(message.chat.id, "Заказать работу:", reply_markup=markup )

        
    





        


   

bot.polling(non_stop=True)