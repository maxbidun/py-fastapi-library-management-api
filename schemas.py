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


class AutorBase(BookBase):
    name: str
    bio: str
    book_id: int


class AutorCreate(AutorBase):
    pass



class Autor(AutorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
