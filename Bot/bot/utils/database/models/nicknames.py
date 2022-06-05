from sqlalchemy import Column, Integer, String

from .. import Base


class Nickname(Base):
    __tablename__ = "nicknames"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String, unique=True, index=True)
    owner_telegram_id = Column(Integer, index=True)
