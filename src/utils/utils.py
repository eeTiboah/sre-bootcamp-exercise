from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.core.configvars import env_config
from pydantic import BaseModel

class HealthCheck(BaseModel):
    status: str
    database_status: str


DATABASE_URL = f"postgresql+asyncpg://{env_config.DB_USER}:{env_config.DB_PASSWORD}@{env_config.DB_HOST}:5432/{env_config.DB_NAME}"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session