from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

from config import dp, bot
from keyboards import spam_btn, ListOfButtons
from myslq import rasilkas
from utils import Admin


@dp.message_handler(lambda message: False if message.text.startswith('@fghvjbkn_bot ') else True)
async def get_info(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text="Нажми меня", switch_inline_query_current_chat="")
    keyboard.add(switch_button)
    await message.answer('Нажмите кнопку и введи название компании',
                         parse_mode=ParseMode.HTML, reply_markup=keyboard)


@dp.message_handler(state=Admin.password)
async def profil(message: types.Message, state: FSMContext):
    password = message.text
    data = await state.get_data()
    admin = data.get('admin')
    if password == admin:
        keyboard = spam_btn
        await state.update_data(adminP=1)
        await message.answer(
            'Рады приветствовать администратора\n\nДля размешения нового объявления нажмите кнопку "Разместить объявление" [Инструкция]() ',
            reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        await state.reset_state(with_data=False)
    else:
        await message.answer('Поробуйде еще раз')


@dp.message_handler(state=Admin.text)
async def profil(message: types.Message, state: FSMContext):
    text = message.text
    if message.text == 'Назад':
        keyboard = ListOfButtons(text=['Разместить объявление'], align=[1]).reply_keyboard

        await message.answer('Вы отменили создание объявления', reply_markup=keyboard)
        await state.reset_state(with_data=False)
    else:
        # data = await state.get_data()
        # lot = data.get('lot')

        await state.update_data(text=text)
        keyboard = ListOfButtons(text=['Прислать Видео', 'Прислать фото', 'Новый текст', 'Назад'],
                                 align=[2, 2]).reply_keyboard

        await message.answer(
            'Выберите вид поста.\n\nПри нажатии кнопки "*Прислать Видео*" ваше объявление будет состоять из *Видео* *Текста* и *Кнопок*.\n\nПри нажатии кнопки "*Прислать фото*" ваше объявление будет состоять из  *Фото*(1 фото) *Текста* и *Кнопок*\n\nПри нажатии кнопки "*Новый текст*" вы сможете прислать новый текст объявления\n\nКнопка "Назад" вернет вас к созданию объявления',
            reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        await Admin.fid.set()


@dp.message_handler(state=Admin.fid, content_types=['text'])
async def profil(message: types.Message, state: FSMContext):
    if message.text == 'Прислать Видео':
        keyboard = ListOfButtons(text=['Назад'], align=[2, 2]).reply_keyboard
        await message.answer('Пришлите Видео объявления', reply_markup=keyboard)
        await Admin.video.set()
    elif message.text == 'Прислать фото':
        keyboard = ListOfButtons(text=['Назад'], align=[2, 2]).reply_keyboard
        await message.answer('Пришлите Фото', reply_markup=keyboard)
        await Admin.photo.set()
    elif message.text == 'Новый текст':
        keyboard = ListOfButtons(text=['Назад'], align=[2]).reply_keyboard
        await message.answer('Пришлите новый текст объявления\n\nКнопка "*Назад*" отменит создание объявления',
                             reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        await Admin.text.set()
    elif message.text == 'Назад':

        keyboard = ListOfButtons(text=['Разместить объявление'], align=[2]).reply_keyboard

        await message.answer('Вы отменили создание объявления', reply_markup=keyboard)
        await state.reset_state(with_data=False)


@dp.message_handler(state=Admin.photo, content_types=['photo', 'text'])
async def profil(message: types.Message, state: FSMContext):
    if message.photo:
        a = message.photo
        photo = a[1].file_id
        await state.update_data(photo=photo)
        keyboard = ListOfButtons(text=['Предпросмотер', 'Новые фото', 'Назад'], align=[2, 1]).reply_keyboard
        await message.answer(
            'Нажмите кнопку "Предпросмотер",\n\nКнопка "Новые фото" удали из создаваемого объявления  все фото и сможето добавить новые фото\n\nКнопка "Назад" вернет вас к выбору вида поста',
            reply_markup=keyboard)

    elif message.text == 'Предпросмотер':
        data = await state.get_data()
        photo = data.get('photo')
        if photo:
            text = data.get('text')
            if len(text) >= 1024:
                await bot.send_photo(message.chat.id, photo)
                await bot.send_message(message.chat.id, text)
            else:
                await bot.send_photo(message.chat.id, photo, caption=text)
            keyboard = ListOfButtons(text=['Опубликовать', 'Назад', 'Отмена']).reply_keyboard
            await message.answer(
                'Опубликовать отправит ваше сообщение\n\nКнопка "Назад" вернет вас к изменению видео.\nКнопка "Отмена" отменит создания объявления',
                reply_markup=keyboard)
            await Admin.publek.set()
        else:
            await message.answer('С начало пришлите фото, хотябы одно')
    elif message.text == 'Новые фото':
        keyboard = ListOfButtons(text=['Назад'], align=[2, 1]).reply_keyboard
        await state.update_data(photo=None)
        await message.answer('Пришлите новые фотографии.\n\nКнопка "Назад" вернет вас к выбору вида поста')
    elif message.text == 'Назад':
        keyboard = ListOfButtons(text=['Прислать Видео', 'Прислать фото', 'Новый текст', 'Назад'],
                                 align=[2, 2]).reply_keyboard
        await state.update_data(photo=None)
        await message.answer(
            'Выберите вид поста.\n\nПри нажатии кнопки "*Прислать Видео*" ваше объявление будет состоять из *Видео* *Текста* и *Кнопок*.\n\nПри нажатии кнопки "*Прислать фото*" ваше объявление будет состоять из *Фото*(1 фото) *Текста* и *Кнопок*\n\nПри нажатии кнопки "*Новый текст*" вы сможете прислать новый текст объявления\n\nКнопка "Назад" вернет вас к созданию объявления',
            reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        await Admin.fid.set()


@dp.message_handler(state=Admin.video, content_types=['video', 'text'])
async def profil(message: types.Message, state: FSMContext):
    if message.video:
        a = message.video
        video = a['file_id']
        # print(a['file_id'])
        # video.append(a['file_id'])
        await state.update_data(video=video)
        keyboard = ListOfButtons(text=['Предпросмотер', 'Назад']).reply_keyboard
        await message.answer(
            'Нажмите кнопку "Предпросмотер" для просмотра поста\n\nЕсли прислали не то видео или хотите его поменять просто пришлите новое видео\nКнопка "Назад" вернет вас к выбору вида поста',
            reply_markup=keyboard)
        await Admin.video.set()
    elif message.text == 'Предпросмотер':
        # inline_kb_full = InlineKeyboardMarkup(row_width=2)
        # button = InlineKeyboardButton('Посмотреть ✅', url='https://t.me/busiessbroker_bot')
        # button_2 = InlineKeyboardButton('Разместить ➕', url='https://t.me/busiessbroker_bot')
        # inline_kb_full.add(button,button_2)
        data = await state.get_data()
        video = data.get('video')
        text = data.get('text')
        if video:

            if len(text) >= 1024:
                await bot.send_video(message.chat.id, video)
                await bot.send_message(message.chat.id, text)
            else:
                await bot.send_video(message.chat.id, video, caption=text)
            # await bot.send_message(message.chat.id,text,reply_markup=inline_kb_full)
            keyboard = ListOfButtons(text=['Опубликовать', 'Назад', 'Отмена']).reply_keyboard

            await message.answer(
                'Опубликовать отправит ваше сообщение\n\nКнопка "Назад" вернет вас к изменению видео.\nКнопка "Отмена" отменит создания объявления',
                reply_markup=keyboard)
            await Admin.publek.set()
        else:
            await message.answer('С начало пришлите видео.')
    elif message.text == 'Назад':
        keyboard = ListOfButtons(text=['Прислать Видео', 'Прислать фото', 'Новый текст', 'Назад'],
                                 align=[2, 2]).reply_keyboard
        await state.update_data(photo=None)
        await message.answer(
            'Выберите вид поста.\n\nПри нажатии кнопки "*Прислать Видео*" ваше объявление будет состоять из *Видео* *Текста* и *Кнопок*.\nПри нажатии кнопки "*Прислать фото*" ваше объявление будет состоять из  *Фото*(1 фото) *Текста* и *Кнопок*\nПри нажатии кнопки "*Новый текст*" вы сможете прислать новый текст объявления\nКнопка "Назад" вернет вас к созданию объявления',
            reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        await Admin.fid.set()


@dp.message_handler(state=Admin.publek)
async def profil(message: types.Message, state: FSMContext):
    if message.text == 'Опубликовать':
        # inline_kb_full = InlineKeyboardMarkup(row_width=2)
        # button = InlineKeyboardButton('Посмотреть ✅', url='https://t.me/busiessbroker_bot')
        # button_2 = InlineKeyboardButton('Разместить ➕', url='https://t.me/busiessbroker_bot')
        # inline_kb_full.add(button,button_2)
        data = await state.get_data()
        text = data.get('text')
        rasilka = rasilkas()

        video = data.get('video')
        photo = data.get('photo')
        if photo:
            if len(text) >= 1024:
                for i in rasilka:
                    try:

                        chatid = i['chat_id']
                        await bot.send_photo(chatid, photo)
                        await bot.send_message(chatid, text)
                    except:
                        pass
            else:
                for i in rasilka:
                    try:

                        chatid = i['chat_id']
                        await bot.send_photo(chatid, photo, caption=text)
                    except:
                        pass
            await state.update_data(photo=None)
        elif video:
            if len(text) >= 1024:
                for i in rasilka:
                    try:

                        chatid = i['chat_id']
                        await bot.send_video(chatid, video)
                        await bot.send_message(chatid, text)
                    except:
                        pass
            else:
                for i in rasilka:
                    try:
                        chatid = i['chat_id']
                        await bot.send_video(chatid, video, caption=text)
                    except:
                        pass
            await state.update_data(video=None)
        # await bot.send_video(,video,caption=text,reply_markup=inline_kb_full)
        keyboard = ListOfButtons(text=['Разместить объявление'], align=[1]).reply_keyboard
        len_rasilka = len(rasilka)
        # inline_kb_full = InlineKeyboardMarkup(row_width=2)
        # button_4 = InlineKeyboardButton('Вернуться в канал', url='https://t.me/businessbroker_msk')
        # inline_kb_full.add(button_4)
        await message.answer(f'Рассылка сделанна. Вы отправили {len_rasilka} пользователям')
        await message.answer('Для создания нового объявления нажмите кнопку "Разместить объявление"',
                             reply_markup=keyboard)
        await state.reset_state(with_data=False)
    elif message.text == 'Назад':
        data = await state.get_data()
        photo = data.get('photo')
        video = data.get('video')
        if photo:
            keyboard = ListOfButtons(text=['Назад'], align=[1]).reply_keyboard

            await message.answer(
                'Пришлите Фото объявления (Только одно фото)\n\nКнопка "Назад" вернет вас к выбору вида поста',
                reply_markup=keyboard)
            await Admin.photo.set()
        elif video:
            keyboard = ListOfButtons(text=['Назад'], align=[1]).reply_keyboard
            await message.answer(
                'Пришлите Видео объявления (Только одно видео)\n\nКнопка "Назад" вернет вас к выбору вида поста',
                reply_markup=keyboard)
            await Admin.video.set()
    elif message.text == 'Отмена':

        keyboard = ListOfButtons(text=['Разместить объявление'], align=[1]).reply_keyboard

        await message.answer('Вы отменили создание объявления', reply_markup=keyboard)
        await state.reset_state(with_data=False)
