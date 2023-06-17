from aiogram.dispatcher.filters.state import StatesGroup, State

class Steps(StatesGroup):
    selection = State()
    categories = State()
    calls = State()
    internet = State()
    sms = State()
    social_pass = State()
    social_platforms = State()
