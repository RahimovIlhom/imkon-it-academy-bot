from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

ADMINS = [5232052738, 5442563505]
CHORNIY = []
links = []


@dp.message_handler(chat_id=ADMINS, commands=['createLink'])
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Kalit so'zingizni kiriting: ")
    await state.set_state('crate_link')


@dp.message_handler(state='crate_link')
async def bot_start(message: types.Message, state: FSMContext):
    kalit = message.text
    links.append(str(kalit))
    link = "https://t.me/python_dasturlash_tili2023_bot" + f"?start={kalit}"
    await message.answer(link)
    await state.finish()
