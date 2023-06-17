from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

categories = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Сім'я", callback_data='family'),
            InlineKeyboardButton(text='Студент', callback_data='student')
        ],
        [
            InlineKeyboardButton(text='Дитина', callback_data='child'),
            InlineKeyboardButton(text='Гаджети', callback_data='gadgets')
        ],
        [
            InlineKeyboardButton(text='Особисте користування', callback_data='self')
        ]
    ]
)

calls = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=">1000хв", callback_data='>1000'),
            InlineKeyboardButton(text='<1000хв', callback_data='<1000')
        ],
        [
            InlineKeyboardButton(text='<2000хв', callback_data='<2000'),
            InlineKeyboardButton(text='Безліміт', callback_data='calls_no_limits')
        ],
    ]
)

internet = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=">10ГБ", callback_data='>10'),
            InlineKeyboardButton(text='<10ГБ', callback_data='<10')
        ],
        [
            InlineKeyboardButton(text='<25ГБ', callback_data='<25'),
            InlineKeyboardButton(text='Безліміт', callback_data='internet_no_limits')
        ],
    ]
)


sms = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=">1 SMS", callback_data='>1'),
            InlineKeyboardButton(text='<25 SMS', callback_data='<25')
        ],
        [
            InlineKeyboardButton(text='>25 SMS', callback_data='>25'),
        ],
    ]
)

social_pass = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Так", callback_data='pass_True'),
            InlineKeyboardButton(text='Ні', callback_data='pass_False')
        ]
    ]
)


social_platform = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Так", callback_data='platform_True'),
            InlineKeyboardButton(text='Ні', callback_data='platform_False')
        ]
    ]
)

