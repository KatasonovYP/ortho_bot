from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


cart_1 = InlineKeyboardButton('Ваша корзина пуста', callback_data='empty')


ib_client_cart = InlineKeyboardMarkup()
ib_client_cart.add(cart_1)


def get_catalog_markup(data):
    ib_client_catalog = InlineKeyboardMarkup()
    for item, cnt in zip(data, range(5)):
        if cnt == 5:
            break
        btn = InlineKeyboardButton(text=item['name'], callback_data=f'item_{item["id"]}')
        ib_client_catalog.add(btn)
    btn_left = InlineKeyboardMarkup(text='<', callback_data='catalog_<')
    btn_right = InlineKeyboardMarkup(text='>', callback_data='catalog_>')
    ib_client_catalog.row(btn_left, btn_right)
    return ib_client_catalog


catalog_1 = InlineKeyboardButton(text='add orange', callback_data='add_orange')
catalog_2 = InlineKeyboardButton(text='apple', callback_data='apple')
catalog_3 = InlineKeyboardButton(text='mango', callback_data='mango')
catalog_4 = InlineKeyboardButton(text='kivi', callback_data='kivi')

catalog_5 = InlineKeyboardButton(text='orange', callback_data='orange')
catalog_6 = InlineKeyboardButton(text='apple', callback_data='apple')
catalog_7 = InlineKeyboardButton(text='mango', callback_data='mango')
catalog_8 = InlineKeyboardButton(text='kivi', callback_data='kivi')

ib_client_catalog = InlineKeyboardMarkup()
ib_client_catalog_2 = InlineKeyboardMarkup()
ib_client_catalog.add(catalog_1).add(catalog_2).add(catalog_3).add(catalog_4)
ib_client_catalog_2.add(catalog_5).add(catalog_6).add(catalog_7).add(catalog_8)


product_1 = InlineKeyboardButton('Добавить в корзину', callback_data='add_to_cart')
product_2 = InlineKeyboardButton('Добавить в избранное', callback_data='add_to_favorites')

ib_client_product = InlineKeyboardMarkup()
ib_client_product.row(product_1, product_2)
