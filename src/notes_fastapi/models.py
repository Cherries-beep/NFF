""" SQLAlchemy / ORM модели """

from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base

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

    id  = Column(type_=Integer, primary_key=True, index=True)
    title = Column(type_=String, index=True)
    content = Column(type_=String)
    created_at = Column(DateTime, server_default=func.now()) # значение будет назначено самой бд