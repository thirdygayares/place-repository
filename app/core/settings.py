from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str
    DATABASE_URL: str
    CORS_ALLOWED_ORIGINS: List[str] = []

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
