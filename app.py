from aiogram import executor, types
from aiogram.dispatcher.filters import CommandStart

from GAME_OF_TEENS.keyboards.reply.reply_keyboard import s
from loader import dp, bot
from GAME_OF_TEENS.utils.misc.admins_notify import on_startup_notify
from GAME_OF_TEENS.utils.misc.commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


@dp.message_handler(CommandStart(), state=None)
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, '👋Привіт, {}!👋\n'
                                            'Це бот для підбору вигідного тарифного плану Lifecell.😃\n'
                                            'Для того, щоб підібрати тарифний план потрібно пройти невелике опитування в боті.\n'.format(message.from_user.first_name), reply_markup=s)
    print(message.chat.id)


@dp.message_handler(content_types=['text'])
async def create_resume(message: types.Message):
    if message.text == '📄Підбор тарифного плану📄':
        print('OK')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
