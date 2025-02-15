from dotenv import dotenv_values
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import Database

token = dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token=token)
storage = MemoryStorage()
database = Database("database.py")
database.create_tables()
dp = Dispatcher(bot , storage=storage)