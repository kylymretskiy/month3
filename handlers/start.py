from aiogram import types , Dispatcher
from aiogram.types import (
    CallbackQuery
)

async def start_command(message: types.Message):
    user = message.from_user

    kb = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Наш адрес", callback_data="address")],
            [types.InlineKeyboardButton(text="Контакты", callback_data="contacts")],
            [types.InlineKeyboardButton(text="Режим работы", callback_data="hours")],
            [types.InlineKeyboardButton(text="О нас", callback_data="aboutus")],
            [types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")],
            [types.InlineKeyboardButton(text="Инстаграм", url="https://geeks.kg")],
            [types.InlineKeyboardButton(text="Оставить отзыв", callback_data="feedback")],
            [types.InlineKeyboardButton(text="Наши вакансии", callback_data="vacancies")],
            [types.InlineKeyboardButton(text="Меню", callback_data="menu")]
    ])

    await message.answer(f"Hello , {user.first_name}" , reply_markup=kb)


async def about_us_handler(callback: CallbackQuery):
    await callback.answer("О нас", show_alert=True)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])