from aiogram import types


async def set_default_commands(dispatcher):
    await dispatcher.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("help", "Вивести команду"),
            types.BotCommand("students", "Тарифи із знижкою для студентів"),
            types.BotCommand("family", "Тарифи для сім'ї"),
            types.BotCommand("gadgets", "Тарифи для гаджетів"),
            types.BotCommand("child", "Тарифи для дітей"),
            types.BotCommand("website", "Перехід до сайту"),
        ]
    )
