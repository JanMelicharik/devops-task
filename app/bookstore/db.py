from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from bookstore.config import settings


def get_database_url() -> str:
    return (
        "postgresql://"
        f"{settings.db_settings.db_user.username}:{settings.db_settings.db_user.password}"
        f"@{settings.db_settings.host}:{settings.db_settings.port}/{settings.db_settings.database}"
    )


engine = create_engine(get_database_url(), connect_args={"options": f"-csearch-path={settings.db_settings.db_schema}"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
