from fastapi import FastAPI, HTTPException
from fastapi.params import Depends, Query
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

app = FastAPI()

def get_db() -> Session:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root() -> dict:
    return {"message": "йобнем?"}


@app.get("/books/", response_model=list[schemas.Book])
def read_books(
        db: Session = Depends(get_db),
        limit: int = Query(10, ge=0, le=100),
        skip: int = Query(0, ge=0)
) -> list[schemas.Book]:
    return crud.get_all_books(db, limit=limit, skip=skip)

@app.post("/books/", response_model=schemas.Book)
def create_book(
        book: schemas.BooksCreate,
        db: Session = Depends(get_db)
):
    return crud.create_book(db, book=book)

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(
        book_id: int,
        db: Session = Depends(get_db)
):
    book = crud.get_book(db, book_id=book_id)
    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    return book

@app.get("/authors/{author_id}/}", response_model=schemas.Autor)
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author(db, author_id=author_id)
    if not author:
        raise HTTPException(
            status_code=404,
            detail="Author not found"
        )
    return author

@app.get("/authors/", response_model=list[schemas.Autor])
def read_authors(
        db: Session = Depends(get_db),
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=0, le=100)
) -> list[schemas.Autor]:
    return crud.get_all_author(db, skip=skip, limit=limit)

@app.post("/authors/", response_model=schemas.Autor)
def create_author(
        author: schemas.AutorCreate,
        db: Session = Depends(get_db)
):
    return crud.create_author(db, author=author)