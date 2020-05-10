from aiogram import types
from aiogram.types import ParseMode
from aiogram.utils.markdown import text, hcode, bold, italic, pre, hbold

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import dp, bot
from keyboards import company_kb_1


@dp.message_handler(lambda message: False if message.text.startswith('@fghvjbkn_bot ') else True)
async def get_info(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text="Нажми меня", switch_inline_query_current_chat="")
    keyboard.add(switch_button)
    await message.answer('Нажмите кнопку и введи название компании',
                         parse_mode=ParseMode.HTML, reply_markup=keyboard)
