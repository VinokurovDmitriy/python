from controller import getSchedule, printItems, itallic_text, bold_text
from loader import dp as dp_text
from loader import db, uc
from aiogram import types


@dp_text.message_handler(text=[uc.contacts])
@dp_text.message_handler(commands=[uc.contacts])
async def answer_start_text(message: types.Message):
    await message.answer(text='Мой адрес не дом и не улица. Мой адрес: Советский Союз')


@dp_text.message_handler(text=[uc.work_schedule])
@dp_text.message_handler(commands=[uc.work_schedule])
async def answer_start_text(message: types.Message):
    await message.answer(text=getSchedule(), parse_mode='HTML')


@dp_text.message_handler(text=[uc.about_bot])
@dp_text.message_handler(commands=[uc.about_bot])
async def answer_start_text(message: types.Message):
    await message.answer(text='<pre>Самый лучший бот тот что был вчера,\n приходил ко мне с ночи до утра</pre>',
                         parse_mode='HTML')


@dp_text.message_handler(content_types=[uc.send_contact])
async def answer_get_contact(message: types.Message):
    if message.from_user.id == message.contact.user_id:
        await message.answer(text='Отлично. Мы записали ваш номер в книгу почетных клиентов')
    else:
        await message.answer(text='Вы указали не свои данные')


@dp_text.message_handler(content_types=[uc.send_location])
async def answer_get_contact(message: types.Message):
    await message.answer(text='Ну все. Теперь мы знаем где вы находитесь. Мы идем к вам дружить')


@dp_text.message_handler(text=[uc.show_all_items])
async def answer_start_text(message: types.Message):
    await message.answer(text=bold_text(itallic_text('В наличии в магазине:\n')) + printItems(db.get_items()),
                         parse_mode='HTML')


@dp_text.message_handler(text=[uc.show_basket])
async def answer_start_text(message: types.Message):
    orders = printItems(db.get_user_orders(message.from_user.id))
    await message.answer(text=bold_text(itallic_text("В вашей корзине")) +
                              f'\n{orders}' if len(orders) > 0 else 'Ваша корзина пуста', parse_mode='HTML')


@dp_text.message_handler(text=[uc.hi])
async def answer_hi(message: types.Message):
    await message.answer(text=f'{uc.hi} {message.from_user.full_name}')
