""" Модуль для работы с бд. CRUD операций через SQLAlchemy """

from sqlalchemy.orm import Session
from models import Note
from src.notes_fastapi.schemas import NoteCreate, NoteUpdate


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    """Возвращает список заметок с пагинацией.

    :param db: Сессия базы данных.
    :type db: Session
    :param skip: Количество записей для пропуска.
    :type skip: int
    :param limit: Максимальное число возвращаемых записей.
    :type limit: int
    :returns: Список заметок.
    :rtype: list[Note]
    """
    return db.query(Note).offset(skip).limit(limit).all()


def get_note(db: Session, note_id: int):
    """Возвращает заметку по её ID.

    :param db: Сессия базы данных.
    :type db: Session
    :param note_id: Идентификатор заметки.
    :type note_id: int
    :returns: Объект Note или ``None``, если запись не найдена.
    :rtype: Note | None
    """
    return db.query(Note).filter(Note.id == note_id).first()


def create_note(db: Session, note: NoteCreate):
    """Создаёт и сохраняет новую заметку

    :param db: сессия бд
    :type db: Session
    :param note: данные для создания заметки
    :type note: NoteCreate
    :returns: Созданная заметка
    :rtype: Note

    """
    db_note = Note(*note.model_dump())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note

def update_note(db: Session, note_id: int, note: NoteUpdate):
    """Обновляет существующую заметку по ID.

       :param db: Сессия базы данных.
       :type db: Session
       :param note_id: Идентификатор заметки.
       :type note_id: int
       :param note: Данные для обновления.
       :type note: NoteUpdate
       :returns: Обновлённая заметка или ``None``.
       :rtype: Note | None
       """
    db_note = db.query(Note).filter(Note.id == note_id).first()
    changes = note.model_dump(exclude_unset=True)

    for key, value in changes.items():
        setattr(db_note, key, value)

    db.commit()
    db.refresh(db_note)

    return db_note

def delete_note(db: Session, note_id: int):
    """Удалить заметку по ID.

        :param db: Сессия базы данных.
        :type db: Session
        :param note_id: Идентификатор заметки.
        :type note_id: int
        :returns: db_note если удаление прошло успешно, иначе None
        :rtype: db_note
    """
    db_note = db.query(Note).filter(Note.id == note_id).first()

    if not db_note:
        return None

    db.delete(db_note)
    db.commit()

    return db_note



