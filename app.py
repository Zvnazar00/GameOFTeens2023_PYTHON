from aiogram import executor, types
from aiogram.dispatcher.filters import CommandStart

from GAME_OF_TEENS.handlers.users.tariff import choose
from GAME_OF_TEENS.keyboards.reply.reply_keyboard import select
from GAME_OF_TEENS.keyboards.inline.inline_keyboards import categories as cat, calls as c, internet as i, sms as s, social_pass as p, social_platform as plat
from loader import dp, bot
from GAME_OF_TEENS.utils.misc.admins_notify import on_startup_notify
from GAME_OF_TEENS.utils.misc.commands import set_default_commands
from GAME_OF_TEENS.states.steps import Steps
from GAME_OF_TEENS.utils.database.connection import session, Database


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


@dp.message_handler(CommandStart(), state=None)
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привіт, {}!👋\n'.format(message.from_user.first_name))
    await bot.send_message(message.from_user.id, 'Я Бот-помічник компанії lifecell')
    await bot.send_message(message.from_user.id, 'Я допоможу вам підібрати вигідний тариф', reply_markup=select)
    session.query(Database).filter_by(id=message.chat.id).delete()
    existing_user = session.query(Database).filter_by(id=message.chat.id).first()
    if existing_user:
        pass
    else:
        # Додати новий запис про користувача в базу даних
        new_user = Database(id=message.chat.id)
        session.add(new_user)
        session.commit()
    await Steps.selection.set()


@dp.message_handler(text="Підбор тарифного плану📄", state=Steps.selection)
async def selection(message: types.Message):
    await bot.send_message(message.from_user.id, 'Для кого ви обираєете тариф?', reply_markup=cat)
    await Steps.categories.set()


@dp.callback_query_handler(state=Steps.categories)
async def categories(callback: types.callback_query):
    if callback.data == 'self':
        await bot.send_message(callback.from_user.id, 'Оберіть потрібну кількість хвилин для дзвінків:', reply_markup=c)
        await Steps.calls.set()


@dp.callback_query_handler(state=Steps.calls)
async def calls(callback: types.callback_query):
    existing_user = session.query(Database).filter_by(id=callback.from_user.id).first()
    if callback.data == '300':
        existing_user.update_info(calls='300')
    if callback.data == '1000':
        existing_user.update_info(calls='1000')
    if callback.data == '2000':
        existing_user.update_info(calls='2000')
    if callback.data == 'calls_no_limits':
        existing_user.update_info(calls='10001')
    session.commit()
    await Steps.internet.set()
    await bot.send_message(callback.from_user.id, 'Оберіть потрібну кількість мобільного інтернету(GB):', reply_markup=i)


@dp.callback_query_handler(state=Steps.internet)
async def internet(callback: types.callback_query):
    existing_user = session.query(Database).filter_by(id=callback.from_user.id).first()
    if callback.data == '1':
        existing_user.update_info(internet='1')
    elif callback.data == '10':
        existing_user.update_info(internet='10')
    if callback.data == '25':
        existing_user.update_info(internet='25')
    if callback.data == 'internet_no_limits':
        existing_user.update_info(internet='10001')
    session.commit()
    await Steps.sms.set()
    await bot.send_message(callback.from_user.id, 'Оберіть потрібну кількість SMS:', reply_markup=s)


@dp.callback_query_handler(state=Steps.sms)
async def sms(callback: types.callback_query):
    existing_user = session.query(Database).filter_by(id=callback.from_user.id).first()
    if callback.data == '0':
        existing_user.update_info(sms='0')
    elif callback.data == '20':
        existing_user.update_info(sms='20')
    if callback.data == '25':
        existing_user.update_info(sms='25')
    session.commit()
    await Steps.social_pass.set()
    await bot.send_message(callback.from_user.id, 'Чи потрібен вам необмежений доступ до соціальних мереж (Facebook, istagram, twitter, viber, telegram, skype, whatsapp ) ?', reply_markup=p)


@dp.callback_query_handler(state=Steps.social_pass)
async def social_pass(callback: types.callback_query):
    existing_user = session.query(Database).filter_by(id=callback.from_user.id).first()
    if callback.data == 'pass_True':
        existing_user.update_info(social_pass=True)
    elif callback.data == 'pass_False':
        existing_user.update_info(social_pass=False)
    session.commit()
    await Steps.social_platforms.set()
    await bot.send_message(callback.from_user.id, 'Чи потрібен вам необмежений доступ до освітніх платформ (Google classroom, teams, zoom, ) ?', reply_markup=plat)


@dp.callback_query_handler(state=Steps.social_platforms)
async def social_platform(callback: types.callback_query):
    existing_user = session.query(Database).filter_by(id=callback.from_user.id).first()
    if callback.data == 'platform_True':
        existing_user.update_info(social_platform=True)
    elif callback.data == 'platform_False':
        existing_user.update_info(social_platform=False)
    session.commit()
    await bot.send_message(callback.from_user.id, choose(callback.from_user.id, 'self'))


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
