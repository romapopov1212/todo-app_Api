from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./database.sqlite3"

settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)