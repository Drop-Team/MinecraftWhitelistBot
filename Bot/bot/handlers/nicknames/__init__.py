from aiogram import Dispatcher

from bot.utils.nicknames_manager import callback_data
from .add_nickname import AddNicknameForm
from .add_nickname import add_nickname_command, get_nickname
from .manage_nicknames import ChangeNicknameForm
from .manage_nicknames import manage_nicknames_command, go_to_nicknames_list_callback, go_to_nickname_callback, \
    delete_nickname_callback, change_nickname_callback, get_changed_nickname


def setup(dp: Dispatcher):
    setup_add_nickname_command(dp)
    setup_my_nicknames_command(dp)


def setup_add_nickname_command(dp: Dispatcher):
    dp.register_message_handler(add_nickname_command, commands=["add_nickname"], is_authorized=True)
    dp.register_message_handler(get_nickname, state=AddNicknameForm.nickname, is_authorized=True)


def setup_my_nicknames_command(dp: Dispatcher):
    def setup_nicknames_list():
        dp.register_callback_query_handler(go_to_nicknames_list_callback,
                                           callback_data.go_to_nicknames_list_cb.filter(), is_authorized=True)

    def setup_nickname_managing():
        dp.register_callback_query_handler(go_to_nickname_callback,
                                           callback_data.go_to_nickname_cb.filter(), is_authorized=True)

    def setup_deleting_nickname():
        dp.register_callback_query_handler(delete_nickname_callback,
                                           callback_data.delete_nickname_cb.filter(), is_authorized=True)

    def setup_changing_nickname():
        dp.register_callback_query_handler(change_nickname_callback,
                                           callback_data.change_nickname_cb.filter(), is_authorized=True)
        dp.register_message_handler(get_changed_nickname, state=ChangeNicknameForm.nickname, is_authorized=True)

    dp.register_message_handler(manage_nicknames_command, commands=["my_nicknames"], is_authorized=True)
    setup_nicknames_list()
    setup_nickname_managing()
    setup_deleting_nickname()
    setup_changing_nickname()
