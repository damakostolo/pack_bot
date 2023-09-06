import telebot
import requests
import json


bot = telebot.TeleBot('6476647584:AAHGHKAHRVudthCWaMmO3vg6AvtMYPMHtoA')
API = '41f603ea75f36db707f7a93ca493571a'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Напиши город что бы узнать погоду')


@bot.message_handler(content_types=['text'])
def get_pogoda(message):
    city = message.text.strip().lower()
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200 :
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Погода на данный момент: {temp} °C')

        image = 'sunny.jpeg' if temp > 17.0 else 'sun.jpg'
        file = open ('./' + image, 'rb')
        bot.send_photo(message.chat.id , file)
    else : 
        bot.reply_to(message, 'город указан не верно')

bot.polling(non_stop=True)
