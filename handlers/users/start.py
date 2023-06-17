from aiogram import types
from GAME_OF_TEENS.keyboards.reply.reply_keyboard import select
from GAME_OF_TEENS.app import bot, dp
from GAME_OF_TEENS.states.steps import Steps
from GAME_OF_TEENS.utils.database.connection import Database, session


@dp.message_handler(commands='start', state='*')
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привіт, {}!👋\n'.format(message.from_user.first_name))
    await bot.send_message(message.from_user.id, 'Я Бот-помічник компанії lifecell')
    await bot.send_message(message.from_user.id, 'Я допоможу вам підібрати вигідний тариф', reply_markup=select)
    session.query(Database).filter_by(user_id=message.chat.id).delete()
    existing_user = session.query(Database).filter_by(user_id=message.chat.id).first()
    if existing_user:
        pass
    else:
        # Додати новий запис про користувача в базу даних
        new_user = Database(user_id=message.chat.id)
        session.add(new_user)
        session.commit()
    await Steps.selection.set()
