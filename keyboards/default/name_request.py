from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

request_name = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

request_name.insert(KeyboardButton(text="Ha"))
request_name.insert(KeyboardButton(text='Yo\'q'))
