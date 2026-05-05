from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/dbname")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret_key")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
