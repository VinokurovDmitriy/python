from aiogram import Bot, Dispatcher
from config import TOKEN

from sql_lite_data import DB

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = DB()

