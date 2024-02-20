from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@postgres:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"options": "-csearch-path=bookstore"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
