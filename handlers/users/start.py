import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentType

from filters import IsPrivate
from keyboards.default.menu import menuButtons
from keyboards.inline import link_markup, link_markup_confirm
from loader import dp, db


@dp.message_handler(CommandStart(), IsPrivate(), state='*')
async def show_channels(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    fullname = message.from_user.full_name
    if db.select_user(user_id):
        await message.answer("Yo'nalishni tanlang:", reply_markup=menuButtons)
        return
    msg = await message.answer(f"Assalomu alaykum {fullname}.\n\n"
                               "‼️ Botdan foydalanish uchun quyidagi tugmani bosing va konkursimizda ishtirok eting\n\n"
                               "Konkursda ishtirok etgandan so'ng ✅ Tekshirish tugmasi ochiladi va uni bosing!",
                               reply_markup=await link_markup(None))
    time.sleep(20)
    await msg.edit_reply_markup(reply_markup=await link_markup_confirm(None))
    await state.set_state("check_button")


@dp.callback_query_handler(state='check_button')
async def check_subs(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    fullname = call.from_user.full_name
    db.add_user(user_id, fullname)
    await call.message.delete()
    await call.message.answer("Yo'nalishni tanlang:", reply_markup=menuButtons)
    await state.finish()


@dp.message_handler(content_types=ContentType.ANY, state='check_button')
async def check_subs(message: types.Message, state: FSMContext):
    await message.delete()
    msg = await message.answer("Iltimos yuqoridagi tugmalardan foydalaning 👆")
    time.sleep(2)
    await msg.delete()
