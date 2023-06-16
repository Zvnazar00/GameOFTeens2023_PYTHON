from aiogram import types
import re
from GAME_OF_TEENS.loader import bot, dp, db
from GAME_OF_TEENS.keyboards.reply import *
from aiogram.types import ContentTypes
from GAME_OF_TEENS.states import Steps


@dp.message_handler(content_types=['text'])
async def create_resume(message: types.Message):
    if message.text == '📄Підбор тарифного плану📄':
        print('OK')
