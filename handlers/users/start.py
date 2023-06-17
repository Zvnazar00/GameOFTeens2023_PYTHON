from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

#from GAME_OF_TEENS.keyboards.reply.reply_keyboard import s
from GAME_OF_TEENS.loader import dp, db, bot
from aiogram.types import ContentTypes
from GAME_OF_TEENS.states.steps import Steps


@dp.message_handler(CommandStart(), state=None)
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, '👋Привіт, {}!👋\n'
                                            'Це бот для підбору вигідного тарифного плану Lifecell.😃\n'
                                            'Для того, щоб підібрати тарифний план потрібно пройти невелике опитування в боті.\n'.format(message.from_user.first_name), reply_markup=s)
    print(message.chat.id)


