import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/dbname")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")

settings = Settings()
