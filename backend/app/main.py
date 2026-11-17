from fastapi import FastAPI, Depends
from app.core.config import settings
from datetime import datetime
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from sqlalchemy import text

app = FastAPI(title=settings.app_name)

@app.get("/")
async def home():
    return {"message": "Welcome to the Job Tracker API"}

@app.get("/health")
async def health(db: Annotated[AsyncSession, Depends(get_db)]):
    await db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "ok"}

@app.get("/about")
async def about():
    return {"app": "Job Tracker", "version":"1.0"}

async def get_time():
    return datetime.now().strftime("%H:%M:%S")

# Demo routes, only for learning depends
@app.get("/time")
async def show_time(now: Annotated[str, Depends(get_time)]):
    # Get the current time as text, like 14:35:20
    return {"time": now}

@app.get("/greeting")
async def greeting(now: Annotated[str, Depends(get_time)]):
    # The line, copied again
    return {"message": f"Hello, it is {now}"}


"""
Depends = function that depends on some data
Injection = feeding that data to the function
"""