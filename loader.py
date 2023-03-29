from aiogram import Bot, Dispatcher, types
from src.database.db import Database
from config  import TOKEN_BOT
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import logging

bot = Bot(token=TOKEN_BOT, parse_mode= types.ParseMode.HTML)#<- &lt; >- &gt; &- &amp;
logging.basicConfig(level=logging.INFO)
dp= Dispatcher(bot, storage=MemoryStorage())
db= Database('src/database/database.db')