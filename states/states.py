from aiogram.dispatcher.filters.state import StatesGroup, State


class PersonData(StatesGroup):
    fullname = State()
    email = State()
    phone = State()
