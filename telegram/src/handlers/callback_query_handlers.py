from controllers import printItem, get_id
from keyboards import navigation_callback, item_keyboard, start_callback, commands_default_keyboard, by_callback
from loader import goods_table, bot
from aiogram import types
from loader import dp as dp_callback
from loader import order_table


@dp_callback.callback_query_handler(navigation_callback.filter(for_data='items'))
async def answer_item(call: types.CallbackQuery):
    item_id = call.data.split(':')[-1]
    item_data = goods_table.get_item(int(item_id))
    text_data = printItem(item_data)
    await bot.edit_message_text(text=text_data, chat_id=call.message.chat.id,
                                message_id=call.message.message_id, parse_mode='HTML')
    await bot.edit_message_reply_markup(reply_markup=item_keyboard(item_id),
                                        chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp_callback.callback_query_handler(start_callback.filter())
async def answer_help_command(call: types.CallbackQuery):
    await call.message.answer(text='Список команд внизу', reply_markup=commands_default_keyboard)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@dp_callback.callback_query_handler(by_callback.filter())
async def answer_help_command(call: types.CallbackQuery):
    item_id = get_id(call)
    user_id = call.from_user.id
    order = goods_table.by_item(user_id, item_id)
    if order:
        order_table.add_order(order)
        await call.message.answer(text='Вы купили 1 ' + goods_table.get_item(item_id)[1])
    else:
        await call.message.answer(text='К сожалению этот товар закончился')
