from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callbackData import lesson_callback, category_callback
from loader import db


def lessons_markup(course_id, category_id):
    markup = InlineKeyboardMarkup(row_width=3)

    # for yordamida
    i = 1
    for lesson in db.select_lessons(category_id):
        markup.insert(
            InlineKeyboardButton(
                text=f"{i}-dars",
                callback_data=lesson_callback.new(
                    course_id=course_id,
                    category_id=category_id,
                    lesson_id=lesson[0]
                )
            )
        )
        i += 1

    markup.add(InlineKeyboardButton(text="🔙 Orqaga", callback_data=lesson_callback.new(course_id=course_id, category_id=category_id, lesson_id='back')))

    return markup


def lesson_markup(course_id, category_id):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔙 Orqaga",
                    callback_data=category_callback.new(
                        course_id=course_id,
                        category_id=category_id
                    )
                ),
            ]
        ],
        row_width=1
    )

    return markup
