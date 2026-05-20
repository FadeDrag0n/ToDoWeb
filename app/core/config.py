from functools import lru_cache
from pydantic_settings import BaseSettings
from pathlib import Path

#app

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    APP_NAME: str = 'ToDoWeb'
    DEBUG: bool = True

    DATABASE_URI: str


    class ConfigDict:
        env_file = BASE_DIR / ".env"
        case_sensitive = True
        extra = "ignore"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()