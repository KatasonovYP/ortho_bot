from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import dp, bot

from keyboards.client_kb import kb_client
from keyboards.client_ib import ib_client_cart, get_catalog_markup, ib_client_product
from data.manager import download


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, text='Ух ты!', reply_markup=kb_client)
    await message.answer('Привет!\nЭтот бот поможет тебе выбрать товар и оформить заказ!')


async def market_catalog(message: types.Message):
    ib_client_catalog = get_catalog_markup(download())
    await bot.send_message(message.from_user.id,
                           'Вот твой каталог >>>',
                           reply_markup=ib_client_catalog)


async def market_cart(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Вот твоя корзина >>>',
                           reply_markup=ib_client_cart)


@dp.callback_query_handler(Text(startswith='item_'))
async def market_item(callback: types.CallbackQuery):
    index = int(callback.data.split('_')[1])
    data = download()
    for item in data:
        if item["id"] == index:
            obj = item
            break
    await bot.send_photo(
        chat_id=callback.from_user.id,
        photo='https://images.unsplash.com/photo-1600009723480-ae9ee0a74709?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
        caption=f'Это *{obj["name"]}*\n'
        f'Цена: *{obj["coast"]}$*\n'
        f'Осталось *{obj["count"]} шт.*',
        reply_markup=ib_client_product,
        parse_mode='Markdown')
    await callback.answer('Вот твой продукт')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(market_catalog, commands=['Каталог'])
    dp.register_message_handler(market_cart, commands=['корзина'])
