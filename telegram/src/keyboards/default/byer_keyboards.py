from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='hellow'),
            KeyboardButton(text='hi')
        ],
        [
            KeyboardButton(text='/redis'),
            KeyboardButton(text='/carrot'),
        ],
        [
            KeyboardButton(text='/help'),
            KeyboardButton(text='/items'),
            KeyboardButton(text='/good_by')
        ],
    ],
    resize_keyboard=True
)
commands_info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/about_bot'),
            KeyboardButton(text='/about_us'),
        ],
        [
            KeyboardButton(text='/contacts'),
            KeyboardButton(text='/work_schedule')
        ],
        [
            KeyboardButton(text='/get_contact', request_contact=True),
            KeyboardButton(text='/get_location', request_location=True)
        ]
    ],
    resize_keyboard=True
)
