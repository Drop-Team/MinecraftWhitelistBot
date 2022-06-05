from aiogram import types

from bot.utils.users.get_user import get_user
from bot.utils.whitelist.manage import get_user_nicknames
from .base import BaseState
from ..callback_data import go_to_nickname_cb


class NicknamesListState(BaseState):
    author_telegram_id: int
    page: int

    def __init__(self, author_telegram_id: int, page: int = 1):
        self.page = page
        self.author_telegram_id = author_telegram_id

    def get_message_text(self) -> str:
        nicknames = get_user_nicknames(self.author_telegram_id)
        limit = get_user(self.author_telegram_id).get_nicknames_limit()
        nicknames_remain = max(0, limit - len(nicknames))
        text = f"You can add <b>{nicknames_remain}</b> more nickname(s) out of <b>{limit}</b> total.\n\n"
        if not nicknames:
            text += "You haven't added any nicknames. Add using /add_nickname."
        else:
            text += "Choose a nickname:"
        return text

    def get_message_keyboard(self) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup(row_width=2)

        nicknames = get_user_nicknames(self.author_telegram_id)

        for nickname in nicknames:
            button = types.InlineKeyboardButton(nickname, callback_data=go_to_nickname_cb.new(nickname=nickname))
            markup.insert(button)
        return markup
