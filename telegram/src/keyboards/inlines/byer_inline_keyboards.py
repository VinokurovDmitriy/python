from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callback_data import start_callback, navigation_callback

start_inline_keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Главное Меню', callback_data=start_callback.new())
        ]
    ]
)


def getNavigationButton(id_item, forward=True):
    text = '>>>' if forward else '<<<'
    return InlineKeyboardButton(text=text, callback_data=navigation_callback.new(for_data='items', id=id_item))


def item_keyboard(index=0, status='small') -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup()
    index_right = str(int(index) + 1)
    index_left = str(int(index) - 1)
    match (status):
        case 'small':
            item_inline_keyboard.add(getNavigationButton(index_right))
        case 'big':
            item_inline_keyboard.add(getNavigationButton(index_left, False))
        case _:
            back = getNavigationButton(index_left, False)
            forward = getNavigationButton(index_right)
            item_inline_keyboard.row(back, forward)
    return item_inline_keyboard
