import logging
from datetime import datetime
import time

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5319696901:AAHpJHHHZ4EF22iQ5Cs0ZmavUqxUCzudPtI'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
count = 3


def checkCount():
    global count
    if count > 1:
        count -= 1
        return f'\nОсталось {count} попыток посчитать числа.'
    else:
        save_log(f'{get_date_time()}: попытка уничтожения земли')
        return False


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Приветмземлянин я инопланетный бот калькулятор. Я буду помогать тебе считать.\n"
        " Для того чтобы узнать что я умею вызови команду /help\n"
        "Но учти, цена за мою помощь - уничтожене земли. Хахаха")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("/sum число1 число2 - Вернет сумму двух чисел\n"
                        "/diff число1 число2 - Вернет разность двух чисел \n"
                        "/div число1 число2 - Вернет частное двух чисел \n"
                        "/mult число1 число2 - Вернет произведение двух чисел \n"
                        "/show_log показать журнал событий"
                        )


@dp.message_handler(commands=['sum'])
async def calc_sum(message: types.Message):
    nums = parse_num(message.text)
    save_log(f'{get_date_time()}: {nums[0]} + {nums[1]}')
    text = f'Сумма чисел {nums[0]} и {nums[1]} равна {nums[0] + nums[1]}\nРовно столько часов осталось существовать твоей жалкой планете.\nЗаряжаем протонные пушки'
    await message.reply(text + checkCount())


@dp.message_handler(commands=['diff'])
async def calc_diff(message: types.Message):
    nums = parse_num(message.text)
    save_log(f'{get_date_time()}: {nums[0]} - {nums[1]}')
    text = f'Разность чисел {nums[0]} и {nums[1]} равна {nums[0] - nums[1]}\nКак раз столько лучей смерти нацелено в сторону земли сейчас.'
    reply = checkCount()
    if reply:
        await message.reply(text + reply)
    else:
        for count_down in range(10, 2, -1):
            await message.answer(f'число попыток закончилось {str(count_down)}')
            time.sleep(1)


@dp.message_handler(commands=['mult'])
async def calc_mult(message: types.Message):
    nums = parse_num(message.text)
    save_log(f'{get_date_time()}: {nums[0]} * {nums[1]}')
    reply = checkCount()
    text = f'Произведение чисел {nums[0]} и {nums[1]} равно {nums[0] * nums[1]}\nРовно столько боевых кораблей еще приближается к вашей орбите.'
    if reply:
        await message.reply(text + reply)
    else:
        for count_down in range(10, 2, -1):
            await message.answer(f'eeee, {str(count_down)}')
            time.sleep(1)


@dp.message_handler(commands=['div'])
async def calc_mult(message: types.Message):
    nums = parse_num(message.text)
    save_log(f'{get_date_time()}: {nums[0]} / {nums[1]}')
    text = f'Частное чисел {nums[0]} и {nums[1]} равно {nums[0] / nums[1]}.\nМожешь загадать столько желаний прежде чем мы начнем атаку. Все равно мы их не будем выполнять хахаха.'
    reply = checkCount()
    if reply:
        await message.reply(text + reply)
    else:
        await test(message)

@dp.message_handler(commands=['show_log'])
async def show_log(message: types.Message):
    try:
        with open('log_bot.txt', 'r', encoding='utf-8') as log:
            log_list = log.open().splitlines()
            msg = log_list[:20]
    except:
        msg = 'Что то поломалось. Уже чиним.'
    await message.reply(msg)


def get_date_time():
    return str(datetime.fromtimestamp(int(time.time())))


def parse_num(msg):
    try:
        nums = msg.split(' ')
        return list(map(int, nums[1:]))
    except:
        return


def save_log(msg):
    with open('log_bot.txt', 'a', encoding='utf-8') as log:
        log.write(f'{msg}\n')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
