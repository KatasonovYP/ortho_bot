"""
Тут будет заголовок
"""


import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types

from create_bot import dp, bot
from handlers import admin, client


"""Logger initialization and logging level setting"""
log = logging.getLogger(__name__)
log.setLevel(os.environ.get('LOGGING_LEVEL', 'info').upper())


async def register_handlers(dp: Dispatcher):
    """Registration all handlers before processing update."""
    # admin.register_handlers_admin(dp)
    client.register_handlers_client(dp)

    log.debug('Handlers are registered.')


async def process_event(event, dp: Dispatcher):
    """Преобразование события AWS Lambda в обновление
    и обработка этого обновления.
    """
    log.debug('Update: ' + str(event))

    Bot.set_current(dp.bot)
    update = types.Update.to_object(event)
    await dp.process_update(update)


async def main(event):
    """Асинхронная оболочка для инициализации 
    бота и диспетчера и запуска последующих функций.
    """
    await register_handlers(dp)
    await process_event(event, dp)
    return 'ok'


def lambda_handler(event, context):
    """AWS Lambda handler."""
    print(event)
    return asyncio.get_event_loop().run_until_complete(main(event))
