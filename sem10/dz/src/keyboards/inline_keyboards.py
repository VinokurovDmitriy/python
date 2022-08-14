from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data_storage import currencies
from .callback_data import currency_callback


def get_button(fr, name):
    direction = 'from' if fr else 'to'
    return currency_callback.new(direction=direction, currency=name)


def get_currencies_buttons(fr=True):
    currency_inline_keyboard = InlineKeyboardMarkup()
    all_buttons = [InlineKeyboardButton(text=name, callback_data=get_button(fr, name)) for name in currencies.keys()]
    currency_inline_keyboard.row(all_buttons[0], all_buttons[1], all_buttons[2], all_buttons[3], all_buttons[4])
    currency_inline_keyboard.row(all_buttons[5], all_buttons[6], all_buttons[7], all_buttons[8], all_buttons[9])
    return currency_inline_keyboard

