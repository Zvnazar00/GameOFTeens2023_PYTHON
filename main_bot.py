import logging

from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from steps import Steps
from keyboards import  *

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6111116545:AAGesouFfZuBRhMB5S4pn7eJIKObkLMkIqs')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    # session.query(ResumeBot).filter_by(id=message.chat.id).delete()
    # session.commit()
    await bot.send_message(message.from_user.id,'👋Привіт, {}!👋\n'
                                            'Це бот для підбору вигідного тарифного плану Lifecell.😃\n'
                                            'Для того, щоб підібрати тарифний план потрібно пройти невелике опитування в боті.\n'.format(message.from_user.first_name), reply_markup=s)
    # existing_user = session.query(ResumeBot).filter_by(id=message.chat.id).first()
    # await state.finish()
    # if existing_user:
    #     pass
    # else:
    #     # Додати новий запис про користувача в базу даних
    #     new_user = ResumeBot(id=message.chat.id)
    #     session.add(new_user)
    #     session.commit()

@dp.message_handler(content_types=['text'])
async def create_resume(message: types.Message):
    if message.text == '📄Підбор тарифного плану📄':
        await bot.send_message(message.from_user.id,'Обирайте ваш вік:', reply_markup=age)
        # # PASSWORD
        # characters = string.ascii_letters + string.digits + string.punctuation
        # password = ''.join(random.choice(characters) for i in range(8))
        # try:
        #     existing_user = session.query(ResumeBot).filter_by(id=message.chat.id).first()
        #     existing_user.update_info(password=password)
        #     session.commit()
        #     await Steps.name_surname.set()
        # except :
        #     await bot.send_message(message.chat.id, 'Виникла помилка')

# async def on_startup(dp):
#     await notify_admins(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)