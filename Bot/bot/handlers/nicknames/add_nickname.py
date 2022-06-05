from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot.utils.users.get_user import get_user
from bot.utils.whitelist.errors import NicknameValidationError, NicknameIsTakenError
from bot.utils.whitelist.manage import add_nickname
from bot.utils.whitelist.manage import get_user_nicknames


class AddNicknameForm(StatesGroup):
    nickname = State()


async def add_nickname_command(msg: types.Message):
    """Add nickname command"""

    user_limits = get_user(msg.from_user.id).get_nicknames_limit()
    user_nicknames = get_user_nicknames(msg.from_user.id)
    if len(user_nicknames) >= user_limits:
        await msg.answer("You have exceeded your nicknames limit. Manage them using /my_nicknames.")
        return

    text = "Enter your nickname:"

    await AddNicknameForm.nickname.set()
    await msg.answer(text)


async def get_nickname(msg: types.Message, state: FSMContext):
    """Nickname handler"""

    try:
        add_nickname(msg.text, msg.from_user.id)
    except NicknameValidationError as e:
        return await msg.answer(e.args[0])
    except NicknameIsTakenError as e:
        return await msg.answer(e.args[0])

    await state.finish()
    await msg.answer("Nickname has been successfully added. You can check it using /my_nicknames.")
