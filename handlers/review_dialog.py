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
    await RestourantReview.name.set()
    await callback.message.answer("Как вас зовут")

async def process_name(message: Message, state: FSMContext):
    name = message.text
    async with state.proxy() as data:
        data["name"] = name
    await RestourantReview.next()
    await message.answer("Ваш инстаграм")

async def process_username(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["instagram_username"] = message.text
    await RestourantReview.next()
    await message.answer("поставьте нам оценку от 1 до 5")

async def process_rate(message: Message, state: FSMContext):
    ms = message.text
    if not ms.isdigit() or int(ms) < 1 or int(ms) > 5:
        await message.answer("Вводите только цифры от 1 до 5!")
        return

    async with state.proxy() as data:
        data["rate"] = message.text
    await RestourantReview.next()
    await message.answer("Дополнительные комментарии/жалоба")

async def process_text(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["extra_comments"] = message.text
    await state.finish()
    await message.answer("Спасибо за отзыв")

def register_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(start_dialog,
    lambda c: c.data == "review")
    dp.register_message_handler(process_name, state = RestourantReview.name)
    dp.register_message_handler(process_username, state = RestourantReview.instagram_username)
    dp.register_message_handler(process_rate, state = RestourantReview.rate)
    dp.register_message_handler(process_text, state = RestourantReview.extra_comments)