from aiogram import Bot, Dispatcher
from names import UserCommands
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sql_lite_data import DB
uc = UserCommands()
storage = MemoryStorage()
bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
db = DB()

