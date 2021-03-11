import os.path
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, exc
from contextlib import contextmanager

PATH = 'log_user_mes.db'

Base = declarative_base()

engine = create_engine(f'sqlite:///{PATH}')


@contextmanager
def session_scope():
    """Создание сессий для транзакций."""
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    try:
        yield session
        session.commit()
    except exc.IntegrityError:
        print('Looks like this model object already exists in the DB')
    except Exception as err:
        session.rollback()
        print('*** Error:\n', err)
    finally:
        session.close()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, nullable=False, unique=True)
    first_name = Column(String(200), nullable=False)
    second_name = Column(String(200), nullable=False)

    def __repr__(self):
        return f"<Model: {self.__tablename__} id: {self.user_id}>"


class Message(Base):
    __tablename__ = 'message'

    msg_id = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)
    created_at = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship('User')

    def __repr__(self):
        return f"<Model: {self.__tablename__} id: {self.msg_id}>"


# При отсутствии БД - ее создание в текущей директории
if not os.path.exists(PATH):
    Base.metadata.create_all(engine)
