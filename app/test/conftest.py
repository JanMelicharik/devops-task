import pytest
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine import create_engine
from bookstore.config import settings
from bookstore.db import get_database_url


@pytest.fixture(scope='session')
def db_engine(request):
    """yields a SQLAlchemy engine which is suppressed after the test session"""
    engine_ = create_engine(get_database_url(), connect_args={"options": f"-csearch-path={settings.db_settings.db_schema}"})

    yield engine_

    engine_.dispose()


@pytest.fixture(scope='session')
def db_session_factory(db_engine):
    """returns a SQLAlchemy scoped session factory"""
    return scoped_session(sessionmaker(bind=db_engine))


@pytest.fixture(scope='session')
def db_session(db_session_factory):
    """yields a SQLAlchemy connection which is rollbacked after the test"""
    session_ = db_session_factory()

    yield session_

    try:
        session_.rollback()
        session_.close()
    except Exception:
        pass
