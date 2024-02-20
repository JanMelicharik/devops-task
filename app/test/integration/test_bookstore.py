from bookstore.models import Book


def test_db(db_session):
    truckers = db_session.query(Book).filter(Book.name == "Truckers").first()
    assert truckers.author == "Terry Pratchett"