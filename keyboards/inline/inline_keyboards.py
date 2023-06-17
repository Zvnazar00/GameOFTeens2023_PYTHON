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
            InlineKeyboardButton(text='Безліміт', callback_data='no_limits')
        ],
    ]
)