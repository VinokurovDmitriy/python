from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

command_default_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton(text='Инфо'),
     KeyboardButton(text='Расшифровка валют'),
     KeyboardButton(text='Конвертировать')]
], resize_keyboard=True)
