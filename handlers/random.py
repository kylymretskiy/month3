from random import choice
from aiogram import types , Dispatcher

names = ("Амир", "Артур", "Мигель", "Кайрат")

# @dp.message_handler(commands=['random'])
async def random_command(message: types.Message):
    random_name = choice(names)
    await message.reply(f"Случайное имя: {random_name}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(random_command, commands=['random'])