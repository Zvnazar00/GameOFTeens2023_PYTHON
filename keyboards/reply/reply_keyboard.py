from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

select = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text='Підбір тарифного плану📄')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
