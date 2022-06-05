from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from bot.utils.database import create_session
from bot.utils.database.models import Nickname
from .errors import NicknameValidationError, NicknameIsTakenError
from .helpers import validate_nickname


def get_user_nicknames(owner_telegram_id: int) -> list[str]:
    session = create_session()
    nicknames_request = select(Nickname).where(Nickname.owner_telegram_id == owner_telegram_id)
    nicknames_objects = session.scalars(nicknames_request).all()
    nicknames = [nickname_obj.nickname for nickname_obj in nicknames_objects]
    return nicknames


def add_nickname(nickname: str, owner_telegram_id: int) -> None:
    if not validate_nickname(nickname):
        raise NicknameValidationError

    session = create_session()
    new_nickname = Nickname(nickname=nickname, owner_telegram_id=owner_telegram_id)
    session.add(new_nickname)

    try:
        session.commit()
    except IntegrityError:
        raise NicknameIsTakenError
    finally:
        session.close()


def delete_nickname(nickname: str, owner_telegram_id: int) -> None:
    if not validate_nickname(nickname):
        raise NicknameValidationError

    session = create_session()
    nickname_request = select(Nickname) \
        .where(Nickname.owner_telegram_id == owner_telegram_id) \
        .where(Nickname.nickname == nickname)
    nickname = session.scalars(nickname_request).one()
    session.delete(nickname)
    session.commit()


def change_nickname(old_nickname: str, new_nickname: str, owner_telegram_id: int) -> None:
    add_nickname(new_nickname, owner_telegram_id)
    delete_nickname(old_nickname, owner_telegram_id)
