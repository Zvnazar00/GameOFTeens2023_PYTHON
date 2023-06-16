import logging

from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from GAME_OF_TEENS.keyboards.reply.reply_keyboard import *
from GAME_OF_TEENS.keyboards.inline.inline_keyboards import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6111116545:AAGesouFfZuBRhMB5S4pn7eJIKObkLMkIqs')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, '👋Привіт, {}!👋\n'
                                            'Це бот для підбору вигідного тарифного плану Lifecell.😃\n'
                                            'Для того, щоб підібрати тарифний план потрібно пройти невелике опитування в боті.\n'.format(message.from_user.first_name), reply_markup=s)

@dp.message_handler(content_types=['text'])
async def create_resume(message: types.Message):
    if message.text == '📄Підбор тарифного плану📄':
        await bot.send_message(message.from_user.id,'Обирайте ваш вік:', reply_markup=age)


# async def on_startup(dp):
#     await notify_admins(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)