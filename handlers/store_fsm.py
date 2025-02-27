from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from db import main_db
import logging



class StoreFSM(StatesGroup):
    name_product = State()
    category = State()
    price = State()
    size = State()
    product_id = State()
    infoproduct = State()
    photo = State()
    collection = State
    submit = State()



async def start_fsm_store(message: types.Message):
    await StoreFSM.name_product.set()
    await message.answer('Напишите название товара: ')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text

    await StoreFSM.next()
    await message.answer('Введите категорию товара:')


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await StoreFSM.next()
    await message.answer('Введите цену товара:')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await StoreFSM.next()
    await message.answer('Размер товара:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await StoreFSM.next()
    await message.answer('Артикул для товара:')


async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await StoreFSM.next()
    await message.answer('Отправьте информацию о товаре:')

async def load_infoproduct(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['infoproduct'] = message.text

    await StoreFSM.next()
    await message.answer('Отправьте фото товара:')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await StoreFSM.next()
    await message.answer('Верный ли данные ?')
    await message.answer_photo(photo=data['photo'],
                               caption=f'Название - {data["name_product"]}\n'
                         f'Категория - {data["category"]}\n'
                         f'Цена - {data["price"]}\n'
                         f'Размер - {data["size"]}\n'
                         f'Артикул - {data["product_id"]}\n')

async def load_collection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["collection"] = message.text
    await StoreFSM.next()
    await message.answer("Верные ли данные?")
    await message.answer_photo(
        photo=data['photo'],
        caption=(
            f'Название - {data["name_product"]}\n'
            f'Категория - {data["category"]}\n'
            f'Цена - {data["price"]}\n'
            f'Размер - {data["size"]}\n'
            f'Артикул - {data["product_id"]}\n'
            f'Описание - {data["info_product"]}\n'
            f'Коллекция - {data["collection"]}'
        )
    )

async def submit_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':
            try:
                await main_db.sql_insert_store(
                    name_product=data['name_product'],
                    price=data['price'],
                    size=data['size'],
                    product_id=data['product_id'],
                    photo=data['photo']
                )
                await main_db.sql_insert_store_details(
                    category=data['category'],
                    product_id=data['product_id']
                )
                await main_db.sql_insert_collection_query(
                    product_id=data['product_id'],
                    collection=data['collection']
                )
                await message.answer('Ваши данные в базе!')
            except Exception as e:
                logger.error(f"Ошибка при добавлении данных в базу: {e}")
                await message.answer("Произошла ошибка при сохранении данных. Попробуйте снова.")
        elif message.text.lower() == 'нет':
            await message.answer('Хорошо, отменено!')
        else:
            await message.answer('Выберите "да" или "нет".')
    await state.finish()


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm,
                                Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(start_fsm_store, commands=['store'])
    dp.register_message_handler(load_name, state=StoreFSM.name_product)
    dp.register_message_handler(load_category, state=StoreFSM.category)
    dp.register_message_handler(load_price, state=StoreFSM.price)
    dp.register_message_handler(load_size, state=StoreFSM.size)
    dp.register_message_handler(load_product_id, state=StoreFSM.product_id)
    dp.register_message_handler(load_infoproduct, state=StoreFSM.infoproduct)
    dp.register_message_handler(load_photo, state=StoreFSM.photo,
                                content_types=['photo'])
    dp.register_message_handler(submit_load, state=StoreFSM.submit)