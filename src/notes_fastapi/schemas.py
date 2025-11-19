""" Pydantic модели для валидации входящих/выходящих данных """

from pydantic import BaseModel


class NoteBase(BaseModel):
    """ Базовая схема заметки.
    Общие поля используемые во входящих и входящих схемах
    """
    title: str
    content: str | None = None


class NoteCreate(NoteBase):
    """ Схема данных для создания заметки. Для POST запросов """
    pass


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

    class Config:
        orm_model = True #  Позволяет возвращать SQLAlchemy объекты напрямую