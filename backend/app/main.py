from fastapi import FastAPI
from sqlalchemy import text
from app.database import Base, engine
from app.api import profile
from app.api.auth import router as auth_router
from app.api.project import router as projects_router
from app.api.skill import router as skills_router
from app.api.experience import router as experiences_router
from app.api.education import router as educations_router
from app.api.certificate import router as certificates_router


import app.models  


app = FastAPI(
    title="Portfolio Management System API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(projects_router)
app.include_router(skills_router)
app.include_router(experiences_router)
app.include_router(educations_router)
app.include_router(certificates_router)
app.include_router(profile.router)

@app.get("/")
def root():
    return {
        "message": "Portfolio Management System API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/database")
def database_test():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {
            "database": "Connected successfully"
        }
    except Exception as e:
        return {
            "database": "Connection failed",
            "error": str(e)
        }