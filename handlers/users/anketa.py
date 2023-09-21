import json
import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import filters

from data.change_file import get_users, write_data
from keyboards.default.menu import menuButtons
from keyboards.default.name_request import request_name
from keyboards.default.phone_button import sendPhone
from keyboards.default.signup import signup
from loader import dp
from states.states import PersonData

EMAIL_REG = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
PHONE_NUM = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{2}[-\s\.]?[0-9]{4,6}$"
CARD_NUM = "(^5[0-9]{12}(?:[0-9]{3})?$)|(^(?:8[1-9][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)|(3[47][0-9]{13})|(^9(?:0[0-9]|[68][0-9])[0-9]{11}$)|(^6(?:011|5[0-9]{2})[0-9]{12}$)|(^(?:2131|1800|35\d{3})\d{11}$)"


@dp.message_handler(commands='signup')
@dp.message_handler(text='Ro\'yxatdan o\'tish', state='ishlama')
async def signup(msg: types.Message, state: FSMContext):
    await msg.reply("Ism familiya sifatida profile fullnameizdan foydalanasizmi?", reply_markup=request_name)
    await state.set_state(PersonData.fullname)


@dp.message_handler(text="Ha", state=PersonData.fullname)
async def signup(msg: types.Message, state: FSMContext):
    name = msg.from_user.full_name
    await state.update_data(
        {'name': name}
    )
    await msg.answer("Emailingizni kiriting: ", reply_markup=ReplyKeyboardRemove())
    # await state.set_state(PersonData.email)
    await PersonData.next()


@dp.message_handler(text="Yo'q", state=PersonData.fullname)
async def signup(msg: types.Message, state: FSMContext):
    await msg.answer("Ism familiyangizni yuboring:", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=PersonData.fullname)
async def signup(msg: types.Message, state: FSMContext):
    name = msg.text
    await state.update_data(
        {'name': name}
    )
    await msg.answer("Emailingizni kiriting: ")
    # await state.set_state(PersonData.email)
    await PersonData.next()


@dp.message_handler(filters.Regexp(EMAIL_REG), state=PersonData.email)
async def signup(msg: types.Message, state: FSMContext):
    email = msg.text
    await state.update_data(
        {'email': email}
    )
    await msg.answer("Telefongizni kiriting yoki yuboring: ", reply_markup=sendPhone)
    # await state.set_state(PersonData.email)
    await PersonData.next()


@dp.message_handler(state=PersonData.email)
async def signup(msg: types.Message, state: FSMContext):
    await msg.answer("Email xato qayta kiriting:")


# @dp.message_handler(filters.IsSenderContact(True), content_types='contact')
@dp.message_handler(content_types='contact', is_sender_contact=True, state=PersonData.phone)
@dp.message_handler(filters.Regexp(PHONE_NUM), state=PersonData.phone)
async def signup(msg: types.Message, state: FSMContext):
    if msg.text:
        phone = msg.text
    else:
        phone = msg.contact.phone_number
    await state.update_data(
        {'phone': phone}
    )
    data = await state.get_data()
    data.update({'id': msg.from_user.id})
    users_data = get_users()
    for user in users_data:
        if user['id'] == data['id']:
            users_data.remove(user)
    users_data.append(data)
    response = write_data(users_data)

    xabar = f"ismingiz: {data['name']}\n" \
            f"email: {data['email']}\n" \
            f"phone: {data['phone']}"
    await msg.answer("Ro'yxatdan o'tdingiz! \n"
                     f"Sizning ma'lumotlaringiz: \n{xabar}")
    await msg.answer("Botdan foydalanishingiz mumkin.", reply_markup=menuButtons)
    await state.finish()


@dp.message_handler(state=PersonData.phone)
async def signup(msg: types.Message, state: FSMContext):
    await msg.answer("Telefon nomer xato qayta kiriting:")
