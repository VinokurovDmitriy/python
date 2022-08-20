from controller import bold_text, itallic_text, printItem
from loader import dp, db
from aiogram import types
from keyboards import commands_default_keyboard, commands_info_keyboard

from keyboards import start_inline_keyboard, item_keyboard
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Привет {message.from_user.full_name} 👋', reply_markup=start_inline_keyboard)


@dp.message_handler(text='В магазин 👉')
async def answer_item_command(message: types.Message):
    item = db.get_first()
    count_in_basket = db.check_item_in_basket(message.from_user.id, item[0])
    count_message = 0 if not count_in_basket else count_in_basket[-1]
    await message.answer(text=f'{printItem(item)}\n{bold_text("🗑 В вашей корзине:")} {itallic_text(count_message)}',
                         reply_markup=item_keyboard(item[0]))


@dp.message_handler(commands='help')
async def answer_start_command(message: types.Message):
    await message.answer(text='Список комманд представлен на клавиатуре ⬇', reply_markup=commands_default_keyboard)


@dp.message_handler(text='info')
@dp.message_handler(commands='info')
async def answer_start_command(message: types.Message):
    await message.answer(text='Вы можете получить дополнительную информацию\nжмакнув на кнопки внизу 📖',
                         reply_markup=commands_info_keyboard)


@dp.message_handler(text=['О нас'])
@dp.message_handler(commands=['О_нас'])
async def answer_start_text(message: types.Message):
    await message.answer(text='Мы сделали для вас бота. Мы молодцы ❤', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text=['Главное меню 👑'])
async def answer_start_text(message: types.Message):
    await message.answer(text='Переход в главное меню 🏃🏻‍', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='.', reply_markup=commands_default_keyboard)


