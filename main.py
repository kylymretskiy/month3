import asyncio
from handlers import (
    start ,
    random ,
    my_info,
    review_dialog
)
from bot_config import dp , database

async def onstartup(_):
    database.create_tables()

async def main():
    start.register_handlers(dp)
    random.register_handlers(dp)
    my_info.register_handlers(dp)
    review_dialog.register_handlers(dp)
    await dp.start_polling(onstartup=onstartup)

    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())