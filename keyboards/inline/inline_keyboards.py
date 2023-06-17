from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

categories = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Сім'я", callback_data='family'),
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
            InlineKeyboardButton(text="Від 300хв", callback_data='300'),
            InlineKeyboardButton(text='Від 1000хв', callback_data='1000')
        ],
        [
            InlineKeyboardButton(text='Від 2000хв', callback_data='2000'),
            InlineKeyboardButton(text='Безліміт', callback_data='calls_no_limits')
        ],
    ]
)

internet = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Від 1ГБ", callback_data='1'),
            InlineKeyboardButton(text='Від 10ГБ', callback_data='10')
        ],
        [
            InlineKeyboardButton(text='Від 25ГБ', callback_data='25'),
            InlineKeyboardButton(text='Безліміт', callback_data='internet_no_limits')
        ],
    ]
)


sms = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Без SMS", callback_data='0'),
            InlineKeyboardButton(text='Від 20 SMS', callback_data='20')
        ],
        [
            InlineKeyboardButton(text='Від 25 SMS', callback_data='25'),
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


handmade_but = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Створити свій тариф',
                                 url=r'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/handmade/')
        ]
    ]
)


def create_but(url):
    detail = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Детальніше', url=f'{url}')
            ]
        ]
    )
    return detail
