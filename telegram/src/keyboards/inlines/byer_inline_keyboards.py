from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from controllers import get_next_id
from .callback_data import start_callback, navigation_callback, by_callback

start_inline_keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Главное Меню', callback_data=start_callback.new())
        ]
    ]
)


def get_by_keyboard(id_item) -> InlineKeyboardButton:
    return InlineKeyboardButton(text='Купить', callback_data=by_callback.new(id_item=id_item))


def getNavigationButton(id_item, forward=True):
    text = '>>>' if forward else '<<<'
    return InlineKeyboardButton(text=text, callback_data=navigation_callback.new(for_data='items', id=id_item))

def item_keyboard(good_id) -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup()
    next_good_id = get_next_id(good_id)
    prev_good_id = get_next_id(good_id, False)
    item_inline_keyboard.row(getNavigationButton(prev_good_id, False), getNavigationButton(next_good_id))
    item_inline_keyboard.add(get_by_keyboard(good_id))
    return item_inline_keyboard
