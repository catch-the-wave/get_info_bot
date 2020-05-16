from aiogram.types import CallbackQuery

from config import dp
from keyboards import company_kb_1, company_kb_2, subscribe_kb, unsubscribe_kb
from myslq import smap_up, save_favourites, delete_favourites


@dp.callback_query_handler(lambda call: True)
async def callback_inline(call: CallbackQuery):
    # print(call.i_m_i)
    chat_id = call.message.chat.id
    if call.data == 'add_to_fav':
        first_name = 'Сбербанк'
        inn = '477784566'
        save_favourites(chat_id, first_name, inn)
        await call.message.edit_reply_markup(reply_markup=company_kb_2)
    elif call.data == 'dell_from_fav':
        inn = '477784566'
        delete_favourites(chat_id, inn)
        await call.message.edit_reply_markup(reply_markup=company_kb_1)

    elif call.data == 'download_report':
        f = open('7725352740.pdf', 'rb')
        await call.message.answer_document(f)


    elif call.data == 'unsubscribe':
        smap_up(chat_id, '1')
        await call.message.edit_reply_markup(reply_markup=subscribe_kb)
    elif call.data == 'subscribe':
        smap_up(chat_id)
        await call.message.edit_reply_markup(reply_markup=unsubscribe_kb)
