from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/help'),
            KeyboardButton(text='info'),
        ],
        [
            KeyboardButton(text='В магазин'),
            KeyboardButton(text='Показать все товары'),
            KeyboardButton(text='Показать корзину'),
        ]
    ],
    resize_keyboard=True
)
commands_info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='О боте'),
            KeyboardButton(text='О нас'),
        ],
        [
            KeyboardButton(text='Контакты'),
            KeyboardButton(text='Режим работы')
        ],
        [
            KeyboardButton(text='Отправить контакт', request_contact=True),
            KeyboardButton(text='Отправить местоположение', request_location=True)
        ],
        [
            KeyboardButton(text='Главное меню'),
        ]
    ],
    resize_keyboard=True
)
