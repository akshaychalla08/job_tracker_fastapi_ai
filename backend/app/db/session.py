from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings

# the engine manages our database connections
engine = create_async_engine(settings.database_url) #db connection pool

SessionLocal = async_sessionmaker(engine, expire_on_commit=False) # one session is one request, it takes one idle connection from engine to connect to DB

async def get_db():
    async with SessionLocal() as session:
        yield session