from loader import dp
from aiogram import executor
from aiogram.types import BotCommand
from aiogram.types import AllowedUpdates
from src.handlers import admin, chat
from src.notify import scheduler
import asyncio


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        BotCommand("start", "restart bot"),
        BotCommand("stats", "get user stats"),
        BotCommand("mystats", "get your stats"),
    ])
    

async def start(dp):
    await set_default_commands(dp)
    asyncio.create_task(scheduler())


executor.start_polling(dp, skip_updates=False, on_startup=start, allowed_updates=AllowedUpdates.all())