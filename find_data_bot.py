#!venv/bin/python
from aiogram import executor, types

from config import dp
import handlers
# from db import init_db

###
from config import get_info_bot_token
###


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

