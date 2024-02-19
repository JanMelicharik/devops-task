from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError

from bookstore import models
from bookstore.db import engine


def test_db_connection():
    try:
        with engine.connect():
            return {"message": "DB Works"}
    except OperationalError:
        raise HTTPException(status_code=500, detail="Database connection error")


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books_filtered(db: Session, book_name: str | None, author: str | None, year: int | None, limit: int = 100):
    query = db.query(models.Book)

    if book_name:
        query = query.filter(models.Book.name == book_name)

    if author:
        query = query.filter(models.Book.author == author)

    if year:
        query = query.filter(models.Book.year == year)

    return query.limit(limit).all()
