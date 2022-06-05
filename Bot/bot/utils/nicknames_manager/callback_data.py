from aiogram.utils.callback_data import CallbackData

go_to_nicknames_list_cb = CallbackData("go_to_nicknames_list", "owner_telegram_id")
go_to_nickname_cb = CallbackData("go_to_nickname", "nickname")
delete_nickname_cb = CallbackData("delete_nickname", "nickname")
change_nickname_cb = CallbackData("change_nickname", "nickname")
