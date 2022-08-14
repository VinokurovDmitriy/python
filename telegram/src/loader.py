from aiogram import Bot, Dispatcher
from config import TOKEN
from dataBase.data.data import DataBase

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
data_manager = DataBase()
