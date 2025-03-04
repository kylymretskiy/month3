import asyncio
from handlers import (
    start ,
    random ,
    my_info,
    review_dialog,
    store_fsm,
    send_products,
    edit_products
)
from bot_config import dp , database
from db.main_db import create_tables

async def main():
    start.register_handlers(dp)
    random.register_handlers(dp)
    my_info.register_handlers(dp)
    review_dialog.register_handlers(dp)
    database.create_tables()
    store_fsm.register_handlers(dp)
    send_products.register_handlers(dp)
    edit_products.register_handlers(dp)

    await dp.start_polling()
    await create_tables()

if __name__ == "__main__":
    asyncio.run(main())

