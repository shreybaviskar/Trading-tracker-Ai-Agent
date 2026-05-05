import os
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from core.config import settings
from database.session import get_db
from api.routes import router as api_router
from core.logger import logger

app = FastAPI()

# Dependency to provide a database session
async def db():
    async with get_db() as session:
        yield session

@app.on_event("startup")
async def startup_event():
    logger.info("Application is starting up")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

app.include_router(api_router, prefix="/api")
