from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from controller import get_next_id
from .callback_data import start_callback, navigation_callback, by_callback, count_items_callback
from loader import uc
start_inline_keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text=uc.main_menu, callback_data=start_callback.new())
        ]
    ]
)


def get_by_keyboard(good_id) -> InlineKeyboardButton:
    return InlineKeyboardButton(text='Купить', callback_data=by_callback.new(good_id=good_id))


def getNavigationButton(good_id, forward=True):
    text = '>>>' if forward else '<<<'
    return InlineKeyboardButton(text=text, callback_data=navigation_callback.new(for_data='items', good_id=good_id))


def get_change_count(good_id, increase=True):
    text = '-' if not increase else '+'
    return InlineKeyboardButton(text=text, callback_data=count_items_callback.new(type_change=text, good_id=good_id))


def item_keyboard(good_id) -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup()
    next_good_id = get_next_id(good_id)
    prev_good_id = get_next_id(good_id, False)
    item_inline_keyboard.row(getNavigationButton(prev_good_id, False), getNavigationButton(next_good_id))
    item_inline_keyboard.row(get_change_count(good_id, False), get_change_count(good_id))
    item_inline_keyboard.add(get_by_keyboard(good_id))
    return item_inline_keyboard
