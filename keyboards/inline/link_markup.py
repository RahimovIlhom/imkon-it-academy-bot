import time

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import db


async def link_markup(value):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.insert(
        InlineKeyboardButton(text="Ishtirok etish", url='https://t.me/konkursntbot?start=1332582307')
    )

    return markup


async def link_markup_confirm(value):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.insert(
        InlineKeyboardButton(text="Ishtirok etish", url='https://t.me/konkursntbot?start=1332582307')
    )
    markup.insert(
        InlineKeyboardButton(text='✅ Tekshirish', callback_data='check_button')
    )

    return markup