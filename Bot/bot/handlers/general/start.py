from aiogram import types

from bot.utils.users.get_user import get_user


async def start_command(msg: types.Message):
    """Send start message"""

    text = "Welcome to InnoMinecraftBot.\n" \
           "❓ Use /help for more information.\n\n"

    if await get_user(msg.from_user.id).is_authorized():
        text += "You are already authorized via InnoID, use /add_nickname command to add your nickname."
        await msg.answer(text)
    else:
        text += "First you have to authorize. Go to @InnoIDBot and follow its instructions."
        await msg.answer(text)
