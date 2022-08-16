from aiogram import Bot, Dispatcher
from config import TOKEN

from sql_lite_data import ItemsData, OrderData

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
goods_table = ItemsData()
order_table = OrderData()
goods_counts = goods_table.get_items()
