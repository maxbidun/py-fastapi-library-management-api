from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Book, Author
from schemas import BooksCreate


def get_all_books(db: Session, skip: int = 0, limit: int = 100):
    return db.scalars(select(Book).offset(skip).limit(limit)).all()


def create_book(db: Session, book: BooksCreate):
    db_book = Book(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

def get_book(db: Session, book_id: int):
    return db.scalars(select(Book).where(Book.id == book_id))

def get_all_author(db: Session, skip: int = 0, limit: int = 100):
    return db.scalars(select(Author).offset(skip).limit(limit)).all()

def get_author(db: Session, author_id: int):
    return db.scalars(select(Author).where(Author.id == author_id))


def create_author(db: Session, author: Author):
    db_author = Author(
        name=author.name,
        bio=author.bio,
        book_id=author.book_id
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)