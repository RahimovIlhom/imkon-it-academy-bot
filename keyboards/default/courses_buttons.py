from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db

computer_course_button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

course1 = KeyboardButton(text="Kompyuterni 0dan o'rganish")
course2 = KeyboardButton(text="Windows darslari")
course3 = KeyboardButton(text="Linux darslari")
course4 = KeyboardButton(text="Kompyuter qismlari")
back = KeyboardButton(text="🔙 Orqaga")

computer_course_button.insert(course1)
computer_course_button.insert(course2)
computer_course_button.insert(course3)
computer_course_button.insert(course4)
computer_course_button.add(back)


graphic_course_button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

course1 = KeyboardButton(text="Adobe Photoshop")
course2 = KeyboardButton(text="Adobe Illustrator")
course3 = KeyboardButton(text="Adobe XD")
course4 = KeyboardButton(text="Figma")

graphic_course_button.insert(course1)
graphic_course_button.insert(course2)
graphic_course_button.insert(course3)
graphic_course_button.insert(course4)
graphic_course_button.add(back)


programming_course_button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

for course in db.select_courses():
    programming_course_button.insert(
        KeyboardButton(text=f'{course[1]}')
    )
programming_course_button.add(back)


smm_course_button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

smm_course_button.add(back)


ai_course_button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

ai_course_button.add(back)


oneC_course_button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

oneC_course_button.add(back)
