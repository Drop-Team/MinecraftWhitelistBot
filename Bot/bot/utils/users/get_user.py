from .user import User

users: list[User] = []


def get_user(telegram_id: int) -> User:
    """Get user by Telegram ID"""

    for user in users:
        if user.telegram_id == telegram_id:
            return user

    user = User(telegram_id)
    users.append(user)
    return user
