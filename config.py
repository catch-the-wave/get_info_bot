import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# get_info_bot_token = os.environ["GET_INFO_BOT_TOKEN"]
get_info_bot_token = '1096481013:AAEXCmHbY44WsA1aOoRe_hu5_u7GCHU2qrY'

bot = Bot(token=get_info_bot_token)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)

logging.basicConfig(level=logging.DEBUG)
