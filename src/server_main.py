"""
Simple echo Telegram Bot example on Aiogram framework using AWS API
Gateway & Lambda.
"""


import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
# Logger initialization and logging level setting
log = logging.getLogger(__name__)
log.setLevel(os.environ.get('LOGGING_LEVEL', 'info').upper())


# Handlers

from create_bot import dp, bot
from handlers import admin, client


async def start(message: types.Message):
    await message.reply('Hello, {}!'.format(message.from_user.first_name))


async def echo(message: types.Message):
    await message.answer(message.text + admin.meow())


# AWS Lambda funcs
async def register_handlers(dp: Dispatcher):
    """Registration all handlers before processing update."""
    # admin.register_handlers_admin(dp)
    client.register_handlers_client(dp)
    # dp.register_message_handler(start, commands=['start'])
    # dp.register_message_handler(echo)

    log.debug('Handlers are registered.')


async def process_event(event, dp: Dispatcher):
    """
    Converting an AWS Lambda event to an update and handling that
    update.
    """

    log.debug('Update: ' + str(event))

    Bot.set_current(dp.bot)
    update = types.Update.to_object(event)
    await dp.process_update(update)


async def main(event):
    """
    Asynchronous wrapper for initializing the bot and dispatcher,
    and launching subsequent functions.
    """

    await register_handlers(dp)
    await process_event(event, dp)

    return 'ok'


def lambda_handler(event, context):
    """AWS Lambda handler."""
    print(event)
    return asyncio.get_event_loop().run_until_complete(main(event))