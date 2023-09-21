from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            # types.BotCommand("signup", "Qayta ro'yxatdan o'tish!"),
            # types.BotCommand("info", "methods!"),
            # types.BotCommand("info_html", "html!"),
            # types.BotCommand("info_markdown", "markdown2!"),
        ]
    )
