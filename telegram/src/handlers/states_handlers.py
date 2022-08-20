from controller import bold_text, printItems, print_quest
from keyboards.default.byer_keyboards import stop_search_keyboard, commands_default_keyboard
from states import BuyerState
from loader import dp as dp_states, db, uc
from aiogram.dispatcher import FSMContext
from datetime import datetime


@dp_states.message_handler(text=[uc.find_item])
async def show_item(message):
    await message.answer(text='Напишите название товара')
    await BuyerState.wait_name_product.set()


@dp_states.message_handler(text=[uc.leave_feedback])
async def start_quest(message):
    await message.answer(text='Будем признательны если вы ответите на 3 вопроса\n' + print_quest(1))
    await BuyerState.start_quest.set()


@dp_states.message_handler(state=BuyerState.wait_name_product)
async def get_itm_name(message, state: FSMContext):
    reply_markup = stop_search_keyboard
    items_info = db.get_items_by_name(message.text)
    if message.text == uc.stop_search:
        await state.reset_state()
        data_text = 'Режим поиска товара отключен'
        reply_markup = commands_default_keyboard
        await state.reset_state()
    elif len(items_info):
        data_text = bold_text('По вашему запросу найдено: \n') + printItems(items_info)
    else:
        data_text = f'Такого товара нет. Попробуйте поискать что то еще или нажмите кнопку \n ' \
                    f'{bold_text("Остановить поиск")} \nчтобы выйти из режима поиска товаров'
    await message.answer(text=data_text, reply_markup=reply_markup)


@dp_states.message_handler(state=BuyerState.start_quest)
async def get_first_answer(message, state: FSMContext):
    await state.update_data(first=message.text)
    await state.reset_state(with_data=False)
    await message.answer(text=print_quest(2))
    await BuyerState.next_quest.set()


@dp_states.message_handler(state=BuyerState.next_quest)
async def get_first_answer(message, state: FSMContext):
    await state.update_data(second=message.text)
    await state.reset_state(with_data=False)
    await message.answer(text=print_quest(3))
    await BuyerState.last_quest.set()



@dp_states.message_handler(state=BuyerState.last_quest)
async def get_first_answer(message, state: FSMContext):
    data = await state.get_data()
    date_now = datetime.now()
    data['user_id'] = message.from_user.id
    data['timestamp'] = f'{date_now.date()} {date_now.time()}'
    result = '\n'.join([f'{key}: {value}' for key, value in data.items()])
    if message.text.isnumeric() and 1 <= int(message.text) <= 10:
        await state.update_data(last=message.text)
        with open('quest.txt', 'a', encoding='utf-8') as f:
            f.write(f'{40*"-"}\n{result})\n{40*"-"}\n')
        await state.reset_state()
        await message.answer('Спасибо за ваш отзыв. Приходите еще')
    else:
        await message.answer(text='Введите корректное значение (число от 1 до 10)')


