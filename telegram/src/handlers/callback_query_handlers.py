from controller import printItem, get_id, printItems
from keyboards import commands_default_keyboard, item_keyboard
from keyboards import navigation_callback, by_callback_callback, count_items_callback, start_callback
from loader import db, bot
from aiogram import types
from loader import dp as dp_callback



@dp_callback.callback_query_handler(navigation_callback.filter(for_data='items'))
async def answer_item(call: types.CallbackQuery):
    item_id = call.data.split(':')[-1]
    item_data = db.get_item(int(item_id))
    text_data = printItem(item_data)
    await bot.edit_message_text(text=text_data, chat_id=call.message.chat.id,
                                message_id=call.message.message_id, parse_mode='HTML')
    await bot.edit_message_reply_markup(reply_markup=item_keyboard(item_id),
                                        chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp_callback.callback_query_handler(start_callback.filter())
async def answer_help_command(call: types.CallbackQuery):
    await call.message.answer(text='Список команд внизу', reply_markup=commands_default_keyboard)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)\

@dp_callback.callback_query_handler(count_items_callback.filter(type_change='+'))
async def answer_help_command(call: types.CallbackQuery):
    item_id = get_id(call)
    user_id = call.from_user.id
    order = db.by_item(item_id)
    if order:
        db.add_order(item_id, user_id)
    else:
        await call.message.answer(text='К сожалению этот товар закончился')
    item_data = db.get_item(int(item_id))
    text_data = printItem(item_data)
    await bot.edit_message_text(text=f'{text_data}\n В вашей корзине {db.check_item_in_basket(user_id,  item_id)[-1]}',
                                chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode='HTML')
    await bot.edit_message_reply_markup(reply_markup=item_keyboard(item_id),
                                        chat_id=call.message.chat.id, message_id=call.message.message_id)

@dp_callback.callback_query_handler(count_items_callback.filter(type_change='-'))
async def answer_help_command(call: types.CallbackQuery):
    item_id = get_id(call)
    user_id = call.from_user.id
    count_in_basket = db.check_item_in_basket(user_id,  item_id)[-1]
    order = db.return_item(item_id, count_in_basket)
    if order:
        db.return_order(item_id, user_id)
    else:
        await call.message.answer(text='В вашей козине больше нет этого товара')
    item_data = db.get_item(int(item_id))
    text_data = printItem(item_data)
    await bot.edit_message_text(text=f'{text_data}\n В вашей корзине {db.check_item_in_basket(user_id,  item_id)[-1]}',
                                chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode='HTML')
    await bot.edit_message_reply_markup(reply_markup=item_keyboard(item_id),
                                        chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp_callback.callback_query_handler(by_callback_callback.filter())
async def answer_help_command(call: types.CallbackQuery):
    user_id = call.from_user.id
    list_items = printItems(db.get_user_orders(user_id))
    text = list_items if list_items else 'Ваша корзина пуста'
    db.del_orders(user_id)
    await call.message.answer(text=f'Вы купили: {text}', parse_mode='HTML')
