class NicknameValidationError(Exception):
    def __init__(self):
        super().__init__("Nickname is invalid.\n"
                         "- It should contain only Latin letters, numbers and underscores.\n"
                         "- Its length should be from 2 to 16 characters.\n"
                         "Try another one.")


class NicknameIsTakenError(Exception):
    def __init__(self):
        super().__init__("Nickname is taken. Try another one.")
