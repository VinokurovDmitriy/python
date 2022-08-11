from aiogram.types import ReplyKeyboardRemove

from controllers import parseItems, setCount, getSchedule
from data import items
from loader import dp
from aiogram import types
from keyboards import commands_default_keyboard, commands_info_keyboard


@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text='Hellow dude')


@dp.message_handler(commands='items')
async def answer_start_command(message: types.Message):
    await message.answer(text=parseItems(), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands='help')
async def answer_start_command(message: types.Message):
    await message.answer(text='Список комманд представлен на клавиатуре', reply_markup=commands_default_keyboard)

@dp.message_handler(commands='info')
async def answer_start_command(message: types.Message):
    await message.answer(text='Вы можете получить дополнительную информацию\nжмакнув на кнопки внизу', reply_markup=commands_info_keyboard)


@dp.message_handler(commands='redis')
async def answer_start_command(message: types.Message):
    await message.answer(text='Редис  ' + str(items['redis']))


@dp.message_handler(commands='Carrot')
async def answer_start_command(message: types.Message):
    await message.answer(text='Морковь  ' + str(items['carrot']))


@dp.message_handler(commands='add')
async def answer_start_command(message: types.Message):
    item = message.text.split(' ')[1]
    setCount(item)
    await message.answer(text='you add ' + str(item))


@dp.message_handler(text=['hi', 'hellow'])
async def answer_start_text(message: types.Message):
    await message.answer(text='dratuti')

@dp.message_handler(commands=['about_us'])
async def answer_start_text(message: types.Message):
    await message.answer(text='Мы сделали для вас бота. Мы молодцы')

@dp.message_handler(commands=['contacts'])
async def answer_start_text(message: types.Message):
    await message.answer(text='Мой адрес не дом и не улица. Мой адрес: Советский Союз')

@dp.message_handler(commands=['work_schedule'])
async def answer_start_text(message: types.Message):
    await message.answer(text=getSchedule())

@dp.message_handler(commands=['about_bot'])
async def answer_start_text(message: types.Message):
    await message.answer(text='Самый лучший бот тот что был вчера,\n приходил ко мне с ночи до утра')


@dp.message_handler(commands=['good_by'])
async def answer_start_text(message: types.Message):
    await message.answer(text='dosvidos')

@dp.message_handler(content_types=['contact'])
async def answer_get_contact(message: types.Message):
    print(message)
    if message.from_user.id == message.contact.user_id:
        await message.answer(text='Отлично. Мы записали ваш номер в книгу почетных клиентов')
    else:
        await message.answer(text='Вы указали не свои данные')

@dp.message_handler(content_types=['location'])
async def answer_get_contact(message: types.Message):
    await message.answer(text='Ну все. Теперь мы знаем где вы находитесь. Мы идем к вам дружить')
