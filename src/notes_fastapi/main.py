""" эндпоинты """
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import get_note, get_notes, create_note, update_note, delete_note
from src.notes_fastapi.crud import get_notes

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/notes/')
def create(title: str, content: str, db: Session = Depends(get_db)):
    return create_note(db=db, title=title, content=content)

@app.get('/notes/')
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_notes(db=db, skip=skip, limit=limit)

@app.get('/notes/{note_id}')
def read_note(note_id: int, db: Session = Depends(get_db)):
    db_note = get_note(db=db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail='Note not found')

    return db_note

@app.put('/notes/{note_id}')
def update(note_id: int, title: str = None, content: str = None, db: Session = Depends(get_db)):
    db_note = update_note(db=db, note_id=note_id, title=title, content=content)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return db_note

@app.delete("/notes/{note_id}")
def delete(note_id: int, db: Session = Depends(get_db)):
    db_note = delete_note(db, note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"message": "Deleted successfully"}
