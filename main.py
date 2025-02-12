import asyncio
from handlers import (
    start ,
    random ,
    my_info,
    review_dialog
)
from aiogram import Bot, Dispatcher
from bot_config import bot , dp

async def main():
    start.register_handlers(dp)
    random.register_handlers(dp)
    my_info.register_handlers(dp)
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())