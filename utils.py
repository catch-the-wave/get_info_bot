from aiogram.dispatcher.filters.state import StatesGroup, State


class Admin(StatesGroup):
    password = State()

    start = State()
    fid = State()
    text = State()
    photo = State()
    video = State()
    publek = State()
