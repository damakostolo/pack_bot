import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('5971340761:AAFCF7-chA51k0Mq-AdgjEjIfoZ4bYYAZNE')
currency = CurrencyConverter()
amout = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message( message.chat.id , 'В ведите сумму для конвертации') 
    bot.register_next_step_handler(message , summa )

def summa(message):
    global amout
    try:
        amout = int(message.text.strip())
    except ValueError :
        bot.send_message(message.chat.id , 'впишите коректную сумму')
        bot.register_next_step_handler(message , summa )
        return


    if amout > 0 :

        markup = types.InlineKeyboardMarkup(row_width= 2)

        btn1 = types.InlineKeyboardButton('USD/EUR' , callback_data= 'usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD' , callback_data= 'usd/eur')
        btn3 = types.InlineKeyboardButton('USD/GBP' , callback_data= 'usd/gbp')
        btn4 = types.InlineKeyboardButton('Другая пара' , callback_data= 'else')

        markup.add(btn1 , btn2 , btn3 , btn4)
        bot.send_message(message.chat.id , 'Выбурите валбтную пару' , reply_markup=markup )
    
    else : 
        bot.send_message(message.chat.id , 'впишите коректную сумму')
        bot.register_next_step_handler(message , summa )



@bot.callback_query_handler(func= lambda call: True)
def callabck(call):
        if call.data != 'else':
            values = call.data.upper().split('/')
            res = currency.convert(amout, values[0] , values[1])
            bot.send_message(call.message.chat.id , f'Ваша сумма: {round(res, 2 )}. Можете указать новую сумму')

            bot.register_next_step_handler(call.message , summa )

        else:
             bot.send_message(call.message.chat.id , 'В ведите валютную пару')
             bot.register_next_step_handler(call.message , mycarrency )


def mycarrency (message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amout, values[0] , values[1])
        bot.send_message(message.chat.id , f'Ваша сумма: {round(res, 2 )}. Можете указать новую сумму')
        bot.register_next_step_handler(message , summa )
    except Exception :
        bot.send_message(message.chat.id , 'впишите коректный формат')
        bot.register_next_step_handler(message , mycarrency )
        return

   

bot.polling(non_stop=True)