""" Pydantic модели для валидации входящих/выходящих данных """
from pydantic import BaseModel
from datetime import datetime


class NoteBase(BaseModel):
    """ Базовая схема заметки. Общие поля используемые во входящих и входящих схемах """
    title: str
    content: str | None = None


class NoteCreate(NoteBase):
    """ Схема данных для создания заметки. Для POST запросов """
    pass


class NoteDetailCreate(BaseModel):
    extra_info: str | None = None


class NoteDetailOut(NoteDetailCreate):
    id: int
    note_id: int

    class Config:
        from_attributes = True


class NoteUpdate(BaseModel):
    """ Схема данных для обновления заметки.

    :param title: новый заголовок заметки
    :rtype title: str | None
    :param content: новое содержимое заметки
    :rtype content: str | None
    """
    title: str | None = None
    content: str | None = None


class NoteOut(NoteBase):
    """Схема данных, возвращаемая API.

        :param id: Идентификатор заметки.
        :type id: int
    """
    id: int
    title: str
    content: str
    created_at: datetime
    detail: NoteDetailOut | None = None

    class Config:
        orm_mode = True #  позволить пайдантик читать SQLAlchemy объекты как словари