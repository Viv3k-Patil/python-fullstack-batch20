from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    year: int


# in memory db
books = [
 {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937
  },
  {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949
  }
]

# read get all books
@app.get('/books')
def get_all_books():
    return books

# read get book by id
@app.get('/books/{book_id}')
def get_book_by_id(book_id: int):
    return books[book_id]

# create add a new book
@app.post('/books')
def create_book(book: Book):
    books.append(book.model_dump())
    return {
        "msg": "success"
    }

# delete delete a book
@app.delete('/books/{book_id}')
def delete_book_by_id(book_id: int):
    books.pop(book_id)
    return {
        "msg": "book deleted successfully"
    }

# update replace a book
@app.put('/books/{book_id}')
def update_book(book_id:int, book: Book):
    book_dict = book.model_dump()
    books[book_id] = book_dict
    return {
        "msg": "success"
    }
