from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔙 Orqaga")],
    ],
    resize_keyboard=True
)