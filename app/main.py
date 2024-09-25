from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import SessionLocal
from app.routers import user, test_db

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(test_db.router, tags=["test"])
app.include_router(user.router, prefix="/users", tags=["users"])