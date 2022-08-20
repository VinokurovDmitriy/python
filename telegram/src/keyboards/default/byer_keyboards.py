from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import uc

commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=uc.start),
            KeyboardButton(text=uc.help),
            KeyboardButton(text=uc.info),
            KeyboardButton(text=uc.hi),
            KeyboardButton(text=uc.leave_feedback),
        ],
        [
            KeyboardButton(text=uc.find_item),
            KeyboardButton(text=uc.to_store),
            KeyboardButton(text=uc.show_all_items),
            KeyboardButton(text=uc.show_basket),
        ]
    ],
    resize_keyboard=True
)

stop_search_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=uc.stop_search)]
    ], resize_keyboard=True
)
commands_info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=uc.about_bot),
            KeyboardButton(text=uc.about_us),
        ],
        [
            KeyboardButton(text=uc.contacts),
            KeyboardButton(text=uc.work_schedule)
        ],
        [
            KeyboardButton(text=uc.send_contact, request_contact=True),
            KeyboardButton(text=uc.send_location, request_location=True)
        ],
        [
            KeyboardButton(text=uc.main_menu),
        ]
    ],
    resize_keyboard=True
)
