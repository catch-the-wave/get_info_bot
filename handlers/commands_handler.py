from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import dp, bot

from keyboards import subscribe_kb


@dp.message_handler(commands="start")
async def show_start_message(message: types.Message):
    await message.answer("Привет! "
                         "Я присылаю информацию о российских компаниях и ИП."
                         )

@dp.message_handler(commands="help")
async def show_start_message(message: types.Message):
    await message.answer("Просто отправьте название компании чтобы получить полную информацию о ней\n")

@dp.message_handler(commands="settings")
async def show_start_message(message: types.Message):
    await message.answer("Настройки\n", reply_markup=subscribe_kb)





