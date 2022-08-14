from aiogram import types

from controllers import *
from keyboards import command_default_keyboard
from keyboards import currency_callback
from keyboards import get_currencies_buttons
from loader import dp, bot


@dp.message_handler(commands=['start'])
async def help_handler(Message: types.Message):
    await Message.reply(text='<pre>Привет. Я бот конвертер валют. Я буду помогать тебе получить курсы валют.\n'
                             'Список команд внизу. Нажми кнопку Инфо чтобы узнать как конвертировать валюты</pre>',
                        reply_markup=command_default_keyboard, parse_mode='HTML')


@dp.message_handler(text=['Инфо'])
async def info_reply(Message: types.Message):
    await Message.reply(text='<i>Для конвертации нужно выполнить 4 простых действия:</i>\n'
                             + get_steps(), parse_mode='HTML')


@dp.message_handler(text=['Расшифровка валют'])
async def info_reply(Message: types.Message):
    await Message.reply(text=get_descriptions_currency(), parse_mode='HTML')


@dp.message_handler(text=['Конвертировать'])
async def convert_reply(Message: types.Message):
    await Message.reply(text=steps[1], parse_mode='HTML',
                        reply_markup=get_currencies_buttons())


@dp.callback_query_handler(currency_callback.filter(direction='from'))
async def save_from(call: types.callback_query):
    currency_from = call.data.split(':')[-1]
    save_help_data('from', currency_from)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer(text=steps[2], reply_markup=get_currencies_buttons(False), parse_mode='HTML')


@dp.callback_query_handler(currency_callback.filter(direction='to'))
async def save_from(call: types.callback_query):
    currency_from = call.data.split(':')[-1]
    save_help_data('to', currency_from)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer(text=steps[3], parse_mode='HTML')


@dp.message_handler(content_types='text')
async def get_count(Message: types.Message):
    if check_help_data() and Message.text.isnumeric():
        save_help_data('count', int(Message.text))
        await Message.reply(get_result_convert())
        reset_help_data()
    else:
        await Message.reply('Введите количество конвертируемой валюты корректно')
