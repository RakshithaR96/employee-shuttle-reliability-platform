from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="Employee Shuttle Reliability Platform API",
    version="0.1.0",
    description="Privacy-preserving shuttle scheduling and reliability platform.",
)

app.include_router(health_router, prefix="/api")


@app.get("/")
def root() -> dict[str, str]:
    return {
        "service": "employee-shuttle-reliability-platform",
        "status": "running",
        "version": app.version,
    }
