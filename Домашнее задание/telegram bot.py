from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('5971340761:AAFCF7-chA51k0Mq-AdgjEjIfoZ4bYYAZNE')
dp = Dispatcher(bot)


@dp.message_handler()
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Основная byaf'))
    markup.add(types.InlineKeyboardButton('Заказать работу'))
    markup.add(types.InlineKeyboardButton('Сотруднричество'))
    await message.answer('Привет выбери пунк в меню :)')


executor.start_polling(dp)
