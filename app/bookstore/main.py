from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from bookstore.crud import get_book, get_books_filtered, test_db_connection
from bookstore.db import SessionLocal

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Welcome to the bookstore!"}


@app.get("/book/{book_id}")
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    return get_book(db, book_id=book_id)


@app.get("/book/")
def get_book_by_attributes(name: str = None, year: int = None, author: str = None, limit: int = None, db: Session = Depends(get_db)):
    result = get_books_filtered(db, book_name=name, author=author, year=year, limit=limit)
    return result


@app.get("/db-connection")
def db_connection():
    return test_db_connection()
