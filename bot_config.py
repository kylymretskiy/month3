from dotenv import dotenv_values
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot , storage=storage)