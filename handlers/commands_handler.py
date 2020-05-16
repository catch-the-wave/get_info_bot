from aiogram import types
from aiogram.dispatcher import FSMContext


from config import dp, bot
from keyboards import subscribe_kb, unsubscribe_kb
from myslq import save_user, smap_not_yes
from utils import Admin


@dp.message_handler(commands="start")
async def show_start_message(message: types.Message):
    try:
        save_user(message)
    except:
        pass
    await message.answer("Привет! "
                         "Я присылаю информацию о российских компаниях и ИП."
                         )


@dp.message_handler(commands="help")
async def show_start_message(message: types.Message):
    await message.answer("Просто отправьте название компании чтобы получить полную информацию о ней\n")


@dp.message_handler(commands="settings")
async def show_start_message(message: types.Message):

    sms = smap_not_yes(message.chat.id)
    if sms == '0':
        keyboard = unsubscribe_kb
    else:
        keyboard = subscribe_kb
    await message.answer("Настройки\n", reply_markup=keyboard)


@dp.message_handler(commands=['admin'])
async def profil(message: types.Message, state: FSMContext):
    await message.answer('Ваш пароль администратора')
    await state.update_data(admin='123')
    await Admin.password.set()



