from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callbackData import category_callback
from loader import db


def categories_markup(course_id):
    categories_inline_buttons = InlineKeyboardMarkup(
        row_width=2,
    )

    for category in db.select_categories(course_id):
        categories_inline_buttons.insert(
            InlineKeyboardButton(
                text=category[1],
                callback_data=category_callback.new(
                    course_id=course_id,
                    category_id=category[0])
            )
        )
    categories_inline_buttons.add(
            InlineKeyboardButton(text="Ulashish 📤",
                                 switch_inline_query="\nDasturlashni o'rganmoqchimisiz?\nUnda bizga qo'shiling!")
    )
    return categories_inline_buttons
