from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton('/Каталог')
b2 = KeyboardButton('/Корзина')
b3 = KeyboardButton('/Мои заказы')
b4 = KeyboardButton('/Расписание')
b5 = KeyboardButton('/Контакты')


kb_client = ReplyKeyboardMarkup()

kb_client.row(b1, b2, b3).row(b4, b5)