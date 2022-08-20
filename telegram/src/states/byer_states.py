from aiogram.dispatcher.filters.state import State, StatesGroup


class BuyerState(StatesGroup):
    wait_name_product = State()
    start_quest = State()
    next_quest = State()
    last_quest = State()
