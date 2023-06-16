from aiogram.dispatcher.filters.state import StatesGroup, State


class Steps(StatesGroup):
    age = State()
    calls = State()
    other_operators = State()
    internet = State()
    sms = State()
    cost = State()
    social_networks = State()