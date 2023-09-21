from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuButtons = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

key1 = KeyboardButton(text="Kompyuter savodxonligi")
key2 = KeyboardButton(text="Grafik dizayn")
key3 = KeyboardButton(text="Dasturlash")
key4 = KeyboardButton(text="SMM va marketing")
key5 = KeyboardButton(text="Sun'iy intellekt")
key6 = KeyboardButton(text="1C bugalteriya")

menuButtons.insert(key1)
menuButtons.insert(key2)
menuButtons.insert(key3)
menuButtons.insert(key4)
menuButtons.insert(key5)
menuButtons.insert(key6)
