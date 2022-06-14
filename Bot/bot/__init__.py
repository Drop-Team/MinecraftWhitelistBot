import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor


async def on_startup(dispatcher: Dispatcher):
    from bot.utils.metrics import metrics

    bot_info = await bot.get_me()
    print(f"Logged in as {bot_info.full_name} ({bot_info.mention})")


def start():
    import bot.utils.database

    from . import filters
    from . import handlers

    filters.setup(dp)

    handlers.general.setup(dp)
    handlers.nicknames.setup(dp)

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
