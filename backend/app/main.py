from fastapi import FastAPI
from sqlalchemy import text
from app.database.database import Base, engine

import app.models  

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Portfolio Management System API",
    version="1.0.0"
)


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