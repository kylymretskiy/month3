import asyncio
from handlers import start , random , my_info
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

token = dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token=token)
dp = Dispatcher(bot)

async def main():
    start.register_handlers(dp)
    random.register_handlers(dp)
    my_info.register_handlers(dp)
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())