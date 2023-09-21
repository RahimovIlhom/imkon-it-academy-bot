from aiogram import types

from loader import dp


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def VideoFilter(msg: types.Message):
    await msg.answer(msg.video.file_id)
