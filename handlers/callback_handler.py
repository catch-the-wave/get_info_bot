from aiogram.dispatcher import FSMContext
from config import dp, bot

from keyboards import company_kb_1, company_kb_2, subscribe_kb, unsubscribe_kb
# import

dp.callback_query_handler

@dp.callback_query_handler(lambda call: True)
async def callback_inline(call, state: FSMContext):
    # print(call.i_m_i)
    i_m_i = call.inline_message_id

    # msg_id = call.
    if call.inline_message_id:
        if call.data == 'add_to_fav':
            await bot.edit_message_reply_markup(inline_message_id=i_m_i, reply_markup=company_kb_2)
        elif call.data == 'dell_from_fav':
            await bot.edit_message_reply_markup(inline_message_id=i_m_i, reply_markup=company_kb_1)

        elif call.data == 'download_report':
            # await bot.send_document(call., 'BQACAgIAAxkBAAM7XrbJnnTK2x8EH_up-C_kZXNH1T4AAq8FAAJJhrhJY8REmuWXg1YZBA')
            pass

        elif call.data == 'unsubscribe':
            await bot.edit_message_reply_markup(inline_message_id=i_m_i, reply_markup=subscribe_kb)
        elif call.data == 'subscribe':
            await bot.edit_message_reply_markup(inline_message_id=i_m_i, reply_markup=unsubscribe_kb)


