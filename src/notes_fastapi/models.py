""" SQLAlchemy / ORM модели """

from sqlalchemy import Column, Integer, String
from database import Base

class Note(Base):
    """Модель таблицы заметок.

        :param id: Уникальный идентификатор заметки.
        :type id: int

        :param title: Заголовок заметки.
        :type title: str

        :param content: Текст заметки.
        :type content: str
    """

    __tablename__ = 'notes'

    note_id = Column(type_=Integer, primary_key=True, index=True)
    title = Column(type_=String, index=True)
    content = Column(type_=String)