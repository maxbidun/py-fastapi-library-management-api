from datetime import date

from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: date
    author_id: int

class BooksCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class AuthorBase(BookBase):
    name: str
    bio: str
    book_id: int


class AuthorCreate(AuthorBase):
    pass



class Author(AuthorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
