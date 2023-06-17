from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from GAME_OF_TEENS.app import dp


@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Почати працювати",
            "/help - Отримати цей список",
            "/students - Тарифи зі знижкою для студентів",
            "/website - Перехід до офіційного сайту")

    await message.answer("\n".join(text))
