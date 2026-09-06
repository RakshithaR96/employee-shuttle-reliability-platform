from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api.routers.cabs import router as cabs_router
from app.api.health import router as health_router
from app.db.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Employee Shuttle Reliability Platform API",
    version="0.2.0",
    description="Privacy-preserving shuttle scheduling and reliability platform.",
    lifespan=lifespan,
)


app.include_router(health_router, prefix="/api")
app.include_router(health_router, prefix="/api")
app.include_router(cabs_router, prefix="/api")

@app.get("/")
def root() -> dict[str, str]:
    return {
        "service": "employee-shuttle-reliability-platform",
        "status": "running",
        "version": app.version,
    }