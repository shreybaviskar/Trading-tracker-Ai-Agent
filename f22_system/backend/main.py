import os
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from core.config import settings
from database.session import get_db

app = FastAPI()

# Dependency to provide a database session
async def db():
    async with get_db() as session:
        yield session

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
