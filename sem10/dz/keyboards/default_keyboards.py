from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

command_default_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton(text='Инфо'), KeyboardButton(text='Конвертировать')]
], resize_keyboard=True)
