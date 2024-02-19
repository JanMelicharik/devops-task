import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database: str = os.getenv("POSTGRES_DB", "book")
    host: str = os.getenv("POSTGRES_HOST", "localhost")
    port: int = os.getenv("POSTGRES_PORT", 5432)
    user: str = os.getenv("POSTGRES_USER", "postgres")
    password: str = os.getenv("POSTGRES_PASSWORD", "password")
    db_schema: str = os.getenv("POSTGRES_SCHEMA", "bookstore")


settings = Settings()
