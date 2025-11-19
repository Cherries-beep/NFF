""" Эндпоинты + зависимости """

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from src.notes_fastapi.crud import get_note, get_notes, create_note, update_note, delete_note
from src.notes_fastapi.crud import get_notes
from src.notes_fastapi.database import engine
from src.notes_fastapi.schemas import NoteCreate, NoteUpdate,  NoteOut
from src.notes_fastapi.models import Base


Base.metadata.create_all(bind=engine) # создание таблиц, если их нет
app = FastAPI()

# Dependency
def get_db():
    """ Возвращает сессию бд. Создает объект SessionLocal, отдает его в виде генератора и закрывает соединение
    после завершения запроса

    :returns: сессия  sqlAlchemy для операций с бд
    :rtype: Session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/notes/', response_model=NoteOut, status_code=status.HTTP_201_CREATED)
async def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    """ Создать заметку

    :param note: заметка
    :type note: NoteCreate
    :param db: Сессия базы данных.
    :type db: Session
    :returns: созданная заметка
    :rtype: NoteOut
    """
    return create_note(db, note)


@app.get('/notes/', response_model=list[NoteOut])
async def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """" Возвращает список заметок.

        :param skip:
        :type skip: int
        :param limit: взять только n строк
        :type limit: int
        :param db: Сессия бд
        :type db: Session
        :returns: список заметок
        :rtype: list[NoteOut]
    """
    return get_notes(db=db, skip=skip, limit=limit)


@app.get('/notes/{note_id}', response_model=NoteOut)
async def read_note(note_id: int, db: Session = Depends(get_db)):
    """" Получить заметку по ID

        :param note_id: id заметки
        :type note_id: int
        :param db: Сессия бд
        :type db: Session
        :rtype: NoteOut
        :raises HTTPException: если заметка не найдена (404)
    """
    note = get_note(db=db, note_id=note_id)

    if note is None:
        raise HTTPException(status_code=404, detail='Note not found')

    return note


@app.put('/notes/{note_id}', response_model=NoteOut)
async def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    """ Обновить заметку по ID

        :param note_id: id заметки
        :type note_id: int
        :param note: заметка
        :type note: NoteUpdate
        :param db: Сессия бд
        :type db: Session
        :returns: NoteOut
        :raises HTTPException: если заметка не найдена (404)
    """
    updated_note = update_note(db=db, note_id=note_id, note=note)

    if updated_note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return updated_note


@app.delete("/notes/{note_id}", response_model=NoteOut)
async def delete(note_id: int, db: Session = Depends(get_db)):
    """ Удаление заметки по ID

        :param note_id: id заметки
        :type note_id: int
        :param db: Сессия бд
        :type db: Session
        :rtype: NoteOut
        :raises HTTPException: если заметка не найдена (404)
    """
    db_note = delete_note(db=db, note_id=note_id)

    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"message": "Deleted successfully"}
