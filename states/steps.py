from aiogram.dispatcher.filters.state import StatesGroup, State


class Steps(StatesGroup):
    select = State()
    categories = State()
    calls = State()
    internet = State()
    sms = State()