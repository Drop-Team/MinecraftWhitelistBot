import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

__factory = None


def database_init(db_file):
    from . import models

    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("No database file specified.")

    connection_string = f"sqlite:///{db_file.strip()}?check_same_thread=False"

    engine = sqlalchemy.create_engine(connection_string)
    __factory = orm.sessionmaker(bind=engine)

    Base.metadata.create_all(engine)


def create_session() -> orm.Session:
    global __factory
    return __factory()


database_init("app.db")
