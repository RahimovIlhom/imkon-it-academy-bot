from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("Noqulaylik uchun uzr so'raymiz!\nBotdan foydalanish uchun qayta sihga tushuring: /start")
