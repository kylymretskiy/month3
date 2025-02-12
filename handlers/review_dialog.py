from aiogram import Dispatcher
from aiogram.types import Message , CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup , State


class RestourantReview(StatesGroup):
    name = State()
    instagram_username = State()
    rate = State()
    extra_comments = State()

async def start_dialog(callback: CallbackQuery):
    await callback.message.answer("Как вас зовут")


def register_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(start_dialog,
    lambda c: c.data == "review")