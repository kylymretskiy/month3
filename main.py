import asyncio
import random
from aiogram import Bot , Dispatcher
from aiogram.types import Message
from dotenv import dotenv_values
from aiogram.utils import executor

token = dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token=token)
dp = Dispatcher(bot)

names = ("Амир", "Артур", "Мигель", "Кайрат")

async def main():
    await dp.start_polling()

@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    user = message.from_user
    await message.answer(f"Hello , {user.first_name}")

@dp.message_handler(commands=['myinfo'])
async def myinfo_command(message: Message):
    user_info = (
        f"Ваш ID: {message.from_user.id}\n"
        f"Ваше имя: {message.from_user.first_name}\n"
        f"Ваш username: @{message.from_user.username if message.from_user.username else 'не указан'}"
    )
    await message.reply(user_info)

@dp.message_handler(commands=['random'])
async def random_command(message: Message):
    random_name = random.choice(names)
    await message.reply(f"Случайное имя: {random_name}")

if __name__ == "__main__":
    asyncio.run(main())