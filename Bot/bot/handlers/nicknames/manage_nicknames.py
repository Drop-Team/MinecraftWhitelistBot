from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot.utils.logs.logger import logger
from bot.utils.metrics.nicknames import nicknames_metrics_update
from bot.utils.nicknames_manager.get_manager import get_manager
from bot.utils.nicknames_manager.manager import NicknamesManager
from bot.utils.nicknames_manager.states import NicknameState, ChangeNicknameState
from bot.utils.whitelist.errors import NicknameValidationError, NicknameIsTakenError
from bot.utils.whitelist.manage import delete_nickname, change_nickname


class ChangeNicknameForm(StatesGroup):
    nickname = State()


async def manage_nicknames_command(msg: types.Message):
    manager = NicknamesManager(msg.from_user.id)
    await manager.send_message(msg.bot, msg.chat.id)


async def go_to_nicknames_list_callback(query: types.CallbackQuery, callback_data: dict):
    manager = get_manager(query.message)
    await manager.update_message()
    await query.answer()


async def go_to_nickname_callback(query: types.CallbackQuery, callback_data: dict):
    manager = get_manager(query.message)
    manager.state = NicknameState(query.message.chat.id, callback_data["nickname"])
    await manager.update_message()
    await query.answer()


async def delete_nickname_callback(query: types.CallbackQuery, callback_data: dict):
    manager = get_manager(query.message)
    nickname = callback_data["nickname"]
    await delete_nickname(nickname, query.message.chat.id)
    await query.answer("Nickname has been successfully deleted.")
    await manager.update_message()

    nicknames_metrics_update()

    logger.info(f"User {query.message.chat.id} deleted nickname '{nickname}'")


async def change_nickname_callback(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    manager = get_manager(query.message)
    manager.state = ChangeNicknameState(query.message.chat.id, callback_data["nickname"])
    await manager.update_message()

    async with state.proxy() as data:
        data["old_nickname"] = callback_data["nickname"]
    await ChangeNicknameForm.nickname.set()

    await query.answer()


async def get_changed_nickname(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        old_nickname = data["old_nickname"]
    new_nickname = msg.text

    try:
        await change_nickname(old_nickname, new_nickname, msg.chat.id)
    except NicknameValidationError as e:
        return await msg.answer(e.args[0])
    except NicknameIsTakenError as e:
        return await msg.answer(e.args[0])

    await state.finish()
    await msg.answer("Nickname has been successfully changed. You can check it using /my_nicknames.")

    logger.info(f"User {msg.chat.id} changed nickname from '{old_nickname}' to '{new_nickname}'")
