from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_data import choice_currency_callback_to, choice_currency_callback_from
from pythonProject.python.sem10.dz.data_storage import currencies


def get_currencies_buttons(fr=True):
    callback = choice_currency_callback_from if fr else choice_currency_callback_to
    all_buttons = [InlineKeyboardButton(text=name, callback_data=callback) for name in currencies.keys()]
    return [all_buttons[:5], all_buttons[5:]]


choice_currency_keyboard_from = InlineKeyboardMarkup(get_currencies_buttons())
choice_currency_keyboard_to = InlineKeyboardMarkup(get_currencies_buttons(False))
