from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os


bot = Bot(os.environ.get('TOKEN'))
dp = Dispatcher(bot)