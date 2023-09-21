import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.inline.callbackData import category_callback, lesson_callback
from keyboards.inline import categories_markup, lessons_markup, lesson_markup
from loader import dp, bot, db


@dp.callback_query_handler(category_callback.filter(), state="program")
async def python_course(call: CallbackQuery, callback_data: dict):
    course_id = callback_data.get('course_id')
    category_id = callback_data.get('category_id')
    await call.message.delete()
    await call.message.answer("Darsni tanlang:", reply_markup=lessons_markup(course_id, category_id))
    await call.answer(cache_time=60)


@dp.callback_query_handler(lesson_callback.filter(), state="program")
async def python_course(call: CallbackQuery, callback_data: dict):
    course_id = callback_data.get('course_id')
    category_id = callback_data.get('category_id')
    lesson_id = callback_data.get('lesson_id')
    await call.message.delete()
    if lesson_id == 'back':
        await call.message.answer("Bo'limni tanglang:", reply_markup=categories_markup(course_id))
        await call.answer(cache_time=60)
        return
    data = db.select_lesson(lesson_id)
    await call.message.answer_video(data[1], caption=data[2], reply_markup=lesson_markup(course_id, category_id))
    await call.answer(cache_time=60)
