"""Файл предназначен для реализации класса пользователя"""

class User:
    user = dict()

    def __init__(self, telegram_id, tag, name, surname):

        self.telegram_id: str = telegram_id
        self.telegram_tag: str = tag
        self.user_name: str = name
        self.surname: str = surname
        self.user_id_db: int = None
        self.rights: bool = None
        self.user_id_rights: int = None

    @classmethod
    def get_user(cls, telegram_id, tag, name, surname):
        if telegram_id in cls.user.keys():
            return cls.user[telegram_id]
        else:
            return cls.add_user(telegram_id, tag, name, surname)

    @classmethod
    def add_user(cls, telegram_id, tag, name, surname):
        cls.user[telegram_id] = User(telegram_id, tag, name, surname)
        return cls.user[telegram_id]
