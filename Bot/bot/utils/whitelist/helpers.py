import re


def validate_nickname(nickname: str):
    """Validate nickname"""
    if not nickname or not isinstance(nickname, str):
        return False

    pattern = r"^[a-zA-Z0-9_]{2,16}$"
    result = re.fullmatch(pattern, nickname)
    if result is not None:
        return True
    else:
        return False
