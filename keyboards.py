from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


s = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text='📄Підбор тарифного плану📄')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


age = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='6-14', callback_data='6-14'),
            InlineKeyboardButton(text='14-18', callback_data='14-18')
        ],
        [
            InlineKeyboardButton(text='18-30', callback_data='18-30'),
            InlineKeyboardButton(text='30-50', callback_data='30-50')
        ],
        [
            InlineKeyboardButton(text='50-60', callback_data='50-60'),
            InlineKeyboardButton(text='>60', callback_data='50-60')
        ]
    ]
)