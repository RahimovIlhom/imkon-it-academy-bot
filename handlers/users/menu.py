from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.back_button import back_button
from keyboards.default.courses_buttons import graphic_course_button, computer_course_button, programming_course_button, \
    smm_course_button, ai_course_button, oneC_course_button
from keyboards.default.menu import menuButtons
from loader import dp


@dp.message_handler(text="Kompyuter savodxonligi")
async def komp_savod(msg: types.Message, state: FSMContext):
    await msg.answer("Darslikni tanlang:", reply_markup=computer_course_button)
    await state.set_state("komp")


@dp.message_handler(text="🔙 Orqaga", state='komp')
async def back_komp(msg: types.Message, state: FSMContext):
    await msg.answer("Kursni tanlang: ", reply_markup=menuButtons)
    await state.finish()


@dp.message_handler(state='komp')
async def back_komp(msg: types.Message, state: FSMContext):
    await msg.answer(msg.text)


@dp.message_handler(text="Grafik dizayn")
async def komp_savod(msg: types.Message, state: FSMContext):
    await msg.answer("Darslikni tanlang:", reply_markup=graphic_course_button)
    await state.set_state("graph")


@dp.message_handler(text="🔙 Orqaga", state='graph')
async def back_komp(msg: types.Message, state: FSMContext):
    await msg.answer("Kursni tanlang: ", reply_markup=menuButtons)
    await state.finish()


@dp.message_handler(state='graph')
async def back_komp(msg: types.Message, state: FSMContext):
    await msg.answer(msg.text)


@dp.message_handler(text="Dasturlash")
async def komp_savod(msg: types.Message, state: FSMContext):
    await msg.answer("Darslikni tanlang:", reply_markup=programming_course_button)
    await state.set_state("program")


@dp.message_handler(text="🔙 Orqaga", state='program')
async def back_komp(msg: types.Message, state: FSMContext):
    await msg.answer("Kursni tanlang: ", reply_markup=menuButtons)
    await state.finish()


@dp.message_handler(text="SMM va marketing")
async def komp_savod(msg: types.Message, state: FSMContext):
    await msg.answer("Darslikni tanlang:", reply_markup=smm_course_button)
    await state.set_state("smm")


@dp.message_handler(text="🔙 Orqaga", state='smm')
async def back_komp(msg: types.Message, state: FSMContext):
    await msg.answer("Kursni tanlang: ", reply_markup=menuButtons)
    await state.finish()


@dp.message_handler(state='smm')
async def back_komp(msg: types.Message, state: FSMContext):
    await msg.answer(msg.text)


@dp.message_handler(text="Sun'iy intellekt")
async def komp_savod(msg: types.Message, state: FSMContext):
    await msg.answer("Darslikni tanlang:", reply_markup=ai_course_button)
    await state.set_state("ai")


@dp.message_handler(text="🔙 Orqaga", state='ai')
async def back_komp(msg: types.Message, state: FSMContext):
    await msg.answer("Kursni tanlang: ", reply_markup=menuButtons)
    await state.finish()


@dp.message_handler(state='ai')
async def back_komp(msg: types.Message, state: FSMContext):
    await msg.answer(msg.text)


@dp.message_handler(text="1C bugalteriya")
async def komp_savod(msg: types.Message, state: FSMContext):
    await msg.answer("Darslikni tanlang:", reply_markup=oneC_course_button)
    await state.set_state("oneC")


@dp.message_handler(text="🔙 Orqaga", state='oneC')
async def back_komp(msg: types.Message, state: FSMContext):
    await msg.answer("Kursni tanlang: ", reply_markup=menuButtons)
    await state.finish()


@dp.message_handler(state='oneC')
async def back_komp(msg: types.Message, state: FSMContext):
    await msg.answer(msg.text)