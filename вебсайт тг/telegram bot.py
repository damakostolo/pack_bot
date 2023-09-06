from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot('5971340761:AAFCF7-chA51k0Mq-AdgjEjIfoZ4bYYAZNE')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open shop', web_app=WebAppInfo(
        url='https://damakostolo.github.io/Negr.Bot/')))

    await message.answer('hello', reply_markup=markup)
    

executor.start_polling(dp)
