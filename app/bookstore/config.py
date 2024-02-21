from pydantic_settings import BaseSettings
from pydantic import BaseModel, ConfigDict


class DbUserSettings(BaseModel):
    username: str
    password: str


class DbSettings(BaseModel):
    database: str
    host: str
    port: str
    db_schema: str
    db_user: DbUserSettings


class Settings(BaseSettings):
    model_config = ConfigDict(env_nested_delimiter="__")
    
    db_settings: DbSettings


settings = Settings()
