from .metrics import nicknames_count_total, users_count_by_nicknames_count

from bot.utils.whitelist.manage import get_all_nicknames


def nicknames_metrics_update():
    nicknames = get_all_nicknames()
    nicknames_count_total.set(len(nicknames))

    nicknames_count_by_user_dict = dict()
    for nickname in nicknames:
        owner = nickname.owner_telegram_id
        nicknames_count_by_user_dict[owner] = nicknames_count_by_user_dict.get(owner, 0) + 1

    users_count_by_nicknames_count.clear()
    for nicknames_count in nicknames_count_by_user_dict.values():
        users_count_by_nicknames_count.labels(str(nicknames_count)).inc()
