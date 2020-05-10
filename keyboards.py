from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


unsubscribe_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Отписаться от рассылки ❌', callback_data='unsubscribe'))

subscribe_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Подписаться на рассылку 📨', callback_data='subscribe'))

company_kb_1 = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Скачать отчет', callback_data='download_report'),
    InlineKeyboardButton('Добавить в избранное ⭐️', callback_data='add_to_fav'))

company_kb_2 = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Скачать отчет', callback_data='download_report'),
    InlineKeyboardButton('Удалить из избранного ❌', callback_data='dell_from_fav'))