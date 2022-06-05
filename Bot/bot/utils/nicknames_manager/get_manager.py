from aiogram import types

from .manager import NicknamesManager


def get_manager(message: types.Message, author_id: int = None) -> NicknamesManager:
    if not author_id:
        author_id = message.chat.id
    return NicknamesManager(author_id, message)
