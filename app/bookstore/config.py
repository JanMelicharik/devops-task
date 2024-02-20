from pydantic_settings import BaseSettings
from pydantic import BaseModel


class DbUserSettings(BaseModel):
    username: str
    password: str


class DbSettings(BaseModel):
    database: str
    host: str
    port: str
    schema: str
    db_user: DbUserSettings


class Settings(BaseSettings):
    db_settings: DbSettings

    class Config:
        env_nested_delimiter = "__"


settings = Settings()
