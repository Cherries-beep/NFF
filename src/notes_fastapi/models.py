""" SQLAlchemy / ORM модели """

from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
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
    created_at = Column(DateTime, server_default=func.now())

    detail = relationship(argument='NoteDetail', back_populates='note', uselist=False) # uselist=False один к одному


class NoteDetail(Base):
    __tablename__ = "note_detail"

    id = Column(Integer, primary_key=True, index=True)
    note_id = Column(Integer, ForeignKey("notes.id"), unique=True)  # связь один к одному
    extra_info = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    note = relationship(argument="Note", back_populates="detail") # связь на уровне python