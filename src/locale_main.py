from aiogram.utils import executor
from create_bot import dp


async def on_start_up(_):
    print('Bot is online!')


from handlers import client, admin, other

from keyboards.client_kb import kb_client
from keyboards.client_ib import ib_client_cart


client.register_handlers_client(dp)
# other.register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
