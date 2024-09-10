from fastapi import FastAPI, Depends, status
from src.routes.student import router
import logging
from src.utils.utils import get_db, HealthCheck
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

app = FastAPI()

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/healthcheck", response_model=HealthCheck, status_code=status.HTTP_200_OK)
async def health_check(db: AsyncSession = Depends(get_db)):
    health_status = "healthy"
    db_status = "up"
    
    try:
        await db.execute(text("SELECT 1"))
        return {
        "status": health_status,
        "database_status": db_status
    }
    except Exception as e:
        health_status = "unhealthy"
        db_status = f"down: {str(e)}"


app.include_router(router, prefix="/api/v1")