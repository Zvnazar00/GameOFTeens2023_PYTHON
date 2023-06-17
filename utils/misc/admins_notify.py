from aiogram import Dispatcher
from GAME_OF_TEENS.data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS.split(','):
        print(admin)
        try:
            await dp.bot.send_message(chat_id=admin, text='Бот працює!')
        except Exception as error:
            print(f'Не вдалося відправити повідолення:{admin}. Помилка: {error}')
