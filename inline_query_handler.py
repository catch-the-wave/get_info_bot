from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle
from config import dp, bot
from aiogram.types import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import text, hcode, bold, italic, pre, hbold
import keyboards
from aiogram.dispatcher.filters.state import State, StatesGroup


import logging
import hashlib


class InlineStates(StatesGroup):
    get_automatic_thought = State()


# @dp.inline_handler(lambda query: len(query.query) > 0)
@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):

    query = inline_query.query or 'Введите название компании'
    query = query.strip().lower()
    # logging.info('inline: %s', query)

    input_content = InputTextMessageContent(query)
    result_id: str = hashlib.md5(query.encode()).hexdigest()

    item = InlineQueryResultArticle(
        id=result_id, title=f'{query!r}',
        input_message_content=InputTextMessageContent(message_text=test_text(query),
                                                      parse_mode=ParseMode.HTML),
        reply_markup=keyboards.company_kb_1
    )

    if query != 'Введите название компании' and (len(query) >= 3):
        print(f'текст: {query}, id: {result_id}, ')
    # don't forget to set cache_time=1 for testing (default is 300s or 5m)
    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)



def test_text(query):
    test_text = text(f"Краткий отчет по ",
                     hcode(f'{query}'),
                     ':\n\n',
                     hbold('ИНН:  '), "{INN_DATA}\n",
                     hbold('ОГРН:  '), "{OGRN_DATA}\n",
                     hbold('КПП:  '), "{KPP_DATA}\n",
                     hbold('др. информация:  '), "{OTHER_DATA}\n",
                     sep=''
                     )
    return test_text