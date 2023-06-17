from aiogram import types
from GAME_OF_TEENS.handlers.users.tariff import choose
from GAME_OF_TEENS.keyboards.inline.inline_keyboards import categories as categ, calls as call, internet as net,\
    sms as s, social_pass as social, social_platform as plat, handmade_but, create_but
from GAME_OF_TEENS.app import dp, bot
from GAME_OF_TEENS.states.steps import Steps
from GAME_OF_TEENS.utils.database.connection import session, Database


@dp.message_handler(text="Підбір тарифного плану📄", state=Steps.selection)
async def selection(message: types.Message):
    await bot.send_message(message.from_user.id, 'Для кого ви обираєете тариф?', reply_markup=categ)
    await Steps.categories.set()


@dp.callback_query_handler(state=Steps.categories)
async def categories(callback: types.callback_query):
    existing_user = session.query(Database).filter_by(user_id=callback.from_user.id).first()
    if callback.data == 'self':
        existing_user.update_info(categories='self')
    elif callback.data == 'family':
        existing_user.update_info(categories='family')
    if callback.data == 'gadgets':
        existing_user.update_info(categories='gadgets')
    await bot.send_message(callback.from_user.id, 'Оберіть потрібну кількість хвилин для дзвінків:', reply_markup=call)
    await Steps.calls.set()


@dp.callback_query_handler(state=Steps.calls)
async def calls(callback: types.callback_query):
    existing_user = session.query(Database).filter_by(user_id=callback.from_user.id).first()
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
    await bot.send_message(callback.from_user.id, 'Оберіть потрібну кількість мобільного інтернету:',
                           reply_markup=net)


@dp.callback_query_handler(state=Steps.internet)
async def internet(callback: types.callback_query):
    existing_user = session.query(Database).filter_by(user_id=callback.from_user.id).first()
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
    existing_user = session.query(Database).filter_by(user_id=callback.from_user.id).first()
    if callback.data == '0':
        existing_user.update_info(sms='0')
    elif callback.data == '20':
        existing_user.update_info(sms='20')
    if callback.data == '25':
        existing_user.update_info(sms='25')
    session.commit()
    await Steps.social_pass.set()
    await bot.send_message(callback.from_user.id, 'Чи потрібен вам необмежений доступ до соціальних мереж?\n'
                                                  '(Facebook, istagram, twitter, viber, telegram, skype, '
                                                  'whatsapp', reply_markup=social)


@dp.callback_query_handler(state=Steps.social_pass)
async def social_pass(callback: types.callback_query):
    existing_user = session.query(Database).filter_by(user_id=callback.from_user.id).first()
    if callback.data == 'pass_True':
        existing_user.update_info(social_pass=True)
    elif callback.data == 'pass_False':
        existing_user.update_info(social_pass=False)
    session.commit()
    await Steps.social_platforms.set()
    await bot.send_message(callback.from_user.id, 'Чи потрібен вам необмежений доступ до освітніх платформ?\n'
                                                  '(Google classroom, teams, zoom)', reply_markup=plat)


@dp.callback_query_handler(state=Steps.social_platforms)
async def social_platform(callback: types.callback_query):
    existing_user = session.query(Database).filter_by(user_id=callback.from_user.id).first()
    if callback.data == 'platform_True':
        existing_user.update_info(social_platform=True)
    elif callback.data == 'platform_False':
        existing_user.update_info(social_platform=False)
    session.commit()
    tariff = choose(callback.from_user.id, existing_user.categories)
    if not tariff:
        await bot.send_message(callback.from_user.id, 'Ми не змогли знайти тариф по вашим вимогам,'
                                                      ' але ви можете створити його самi:')
        photo = open(r'utils\misc\photos\Handmade.jpg', 'rb')
        await bot.send_photo(callback.from_user.id, photo, reply_markup=handmade_but)
    else:
        await bot.send_photo(callback.from_user.id, tariff[0].photo, reply_markup=create_but(tariff[0].url))
        await bot.send_message(callback.from_user.id, 'Тариф <b>{}</b> підібрано для нас за найкращою ціною\n'
                                                      '\n'
                                                      'Ціна: {}Грн / 4 тижні\n'
                                                      'Інтернет: {}ГБ\n'
                                                      'Дзвінки: {}Хв'.format(tariff[0].name,
                                                                             tariff[0].monthly_fee,
                                                                             tariff[0].data_limit,
                                                                             tariff[0].minutes_limit))


@dp.message_handler(commands=['website'], state='*')
async def website(message: types.Message):
    await bot.send_message(message.chat.id, 'Перехід до сайту lifecell')
    await bot.send_message(message.chat.id, 'bit.ly/3JeBQhS')


@dp.message_handler(commands=['student'], state='*')
async def students(message: types.Message):
    await bot.send_message(message.chat.id, 'Перехід до сторінки з інформацією про знижки для студентів')
    await bot.send_message(message.chat.id, 'bit.ly/3Ncp4S3')
