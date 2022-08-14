from loader import dp
from aiogram import types
from keyboards import command_default_keyboard


@dp.message_handler(commands=['start'])
async def help_handler(Message: types.Message):
    await Message.reply(text='Список команд представлен на клавиатуре ниже', reply_markup=command_default_keyboard)


@dp.message_handler(text=['Инфо'])
async def info_reply(Message: types.Message):
    await Message.reply(text='<i>Это бот конвертер валют. Для конвертации нужно выполнить 5 шагов.</i>\n'
                             '<b>Шаг первый:</b> нажмите кнопку Конвертировать в меню\n'
                             '<b>Шаг второй:</b> выберете из какой валюты хотите конвертировать.\n'
                             '<b>Шаг третий:</b> выберете в какую валюту хотите конвертировать\n'
                             '<b>Шаг четвертый:</b> напишите сумму единиц валюты которую хотите конвертировать\n'
                             '<b>Шаг пятый:</b> Нажмите кнопку Получить результат', parse_mode='HTML') \
    @ dp.message_handler(text=['Конвертировать'])


async def convert_reply(Message: types.Message):
    await Message.reply(text='<i>Выберете из какой валюты хотите конвертировать.</i>\n', parse_mode='HTML')
