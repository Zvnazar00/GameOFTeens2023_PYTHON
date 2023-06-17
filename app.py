from aiogram import executor
from loader import dp, bot
from GAME_OF_TEENS.utils.misc.admins_notify import on_startup_notify
from GAME_OF_TEENS.utils.misc.commands import set_default_commands
from GAME_OF_TEENS.handlers.users.tariff import choose


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
