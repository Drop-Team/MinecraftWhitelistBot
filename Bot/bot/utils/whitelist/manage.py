from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from bot.utils.database import create_session
from bot.utils.database.models import Nickname
from . import api
from .errors import NicknameValidationError, NicknameIsTakenError
from .helpers import validate_nickname


def get_all_nicknames() -> list[Nickname]:
    session = create_session()
    nicknames_request = select(Nickname)
    nicknames_objects = session.scalars(nicknames_request).all()
    return nicknames_objects


def get_user_nicknames(owner_telegram_id: int) -> list[str]:
    session = create_session()
    nicknames_request = select(Nickname).where(Nickname.owner_telegram_id == owner_telegram_id)
    nicknames_objects = session.scalars(nicknames_request).all()
    nicknames = [nickname_obj.nickname for nickname_obj in nicknames_objects]
    return nicknames


async def add_nickname(nickname: str, owner_telegram_id: int) -> None:
    if not validate_nickname(nickname):
        raise NicknameValidationError

    nicknames = await api.get_whitelist()
    if any([nickname_data["name"].lower() == nickname.lower() for nickname_data in nicknames]):
        raise NicknameIsTakenError

    session = create_session()
    new_nickname = Nickname(nickname=nickname, owner_telegram_id=owner_telegram_id)
    session.add(new_nickname)

    try:
        session.commit()
    except IntegrityError:
        raise NicknameIsTakenError
    finally:
        session.close()

    await api.add_nickname_to_whitelist(nickname)


async def delete_nickname(nickname: str, owner_telegram_id: int) -> None:
    if not validate_nickname(nickname):
        raise NicknameValidationError

    session = create_session()
    nickname_request = select(Nickname) \
        .where(Nickname.owner_telegram_id == owner_telegram_id) \
        .where(Nickname.nickname == nickname)
    nickname_object = session.scalars(nickname_request).one()
    session.delete(nickname_object)
    session.commit()

    await api.remove_nickname_from_whitelist(nickname)


async def change_nickname(old_nickname: str, new_nickname: str, owner_telegram_id: int) -> None:
    await add_nickname(new_nickname, owner_telegram_id)
    await delete_nickname(old_nickname, owner_telegram_id)
