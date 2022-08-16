from controllers import getSchedule, printItems
from loader import dp as dp_text, goods_table, order_table
from aiogram import types



@dp_text.message_handler(text=['Контакты'])
@dp_text.message_handler(commands=['Контакты'])
async def answer_start_text(message: types.Message):
    await message.answer(text='Мой адрес не дом и не улица. Мой адрес: Советский Союз')


@dp_text.message_handler(text=['Режим работы'])
@dp_text.message_handler(commands=['Режим_работы'])
async def answer_start_text(message: types.Message):
    await message.answer(text=getSchedule(), parse_mode='HTML')


@dp_text.message_handler(text=['О боте'])
@dp_text.message_handler(commands=['О_боте'])
async def answer_start_text(message: types.Message):
    await message.answer(text='<pre>Самый лучший бот тот что был вчера,\n приходил ко мне с ночи до утра</pre>',
                         parse_mode='HTML')


@dp_text.message_handler(content_types=['contact'])
async def answer_get_contact(message: types.Message):
    if message.from_user.id == message.contact.user_id:
        await message.answer(text='Отлично. Мы записали ваш номер в книгу почетных клиентов')
    else:
        await message.answer(text='Вы указали не свои данные')


@dp_text.message_handler(content_types=['location'])
async def answer_get_contact(message: types.Message):
    await message.answer(text='Ну все. Теперь мы знаем где вы находитесь. Мы идем к вам дружить')


@dp_text.message_handler(text=['Показать все товары'])
async def answer_start_text(message: types.Message):
    await message.answer(text=printItems(goods_table.get_items()), parse_mode='HTML')\

@dp_text.message_handler(text=['Показать корзину'])
async def answer_start_text(message: types.Message):
    await message.answer(text='<b><i>В вашей корзине</i></b>\n'
                              f'{printItems(order_table.get_user_orders(message.from_user.id))}', parse_mode='HTML')
