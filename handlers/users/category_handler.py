from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline import categories_markup, category_callback
from loader import dp, bot, db


@dp.message_handler(state="program")
async def python_course(msg: types.Message, state: FSMContext):
    course_name = msg.text
    course = list(filter(lambda name: name[1] == course_name, db.select_courses()))
    if course:
        course_id = course[0][0]
        await msg.answer("Bo'limni tanglang:", reply_markup=categories_markup(course_id))
    else:
        await msg.answer("Iltimos tugmalardan foydalaning!")
