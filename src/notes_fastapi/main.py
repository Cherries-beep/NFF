""" Эндпоинты + зависимости """
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .crud import get_note, get_notes, create_note, update_note, delete_note
from .database import engine
from .schemas import NoteCreate, NoteUpdate,  NoteOut
from .models import Base
from .dependencies import get_db


Base.metadata.create_all(bind=engine) # создание таблиц, если их нет
app = FastAPI()


@app.post('/notes/', response_model=NoteOut, status_code=status.HTTP_201_CREATED)
async def create_note_endpoint(note: NoteCreate, db: Session = Depends(get_db)):
    """ Создать заметку

    :param note: заметка
    :type note: NoteCreate
    :param db: Сессия базы данных.
    :type db: Session
    :returns: созданная заметка
    :rtype: NoteOut
    """
    created_note = create_note(db=db, note=note)

    return created_note


@app.get('/notes/', response_model=list[NoteOut])
async def read_notes_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
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
    all_notes = get_notes(db=db, skip=skip, limit=limit) 

    return all_notes


@app.get('/notes/{note_id}', response_model=NoteOut)
async def read_note_endpoint(note_id: int, db: Session = Depends(get_db)):
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
async def update_note_endpoint(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
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
async def delete_note_endpoint(note_id: int, db: Session = Depends(get_db)):
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

    return db_note