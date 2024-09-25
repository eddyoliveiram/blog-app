from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user_schema import UserCreate, UserOut
from app.repositories.user_repository import get_user_by_username, get_user_by_email, create_user, get_users, update_user, delete_user
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[UserOut])
def read_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users

@router.post("/", response_model=UserOut)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user_by_username = get_user_by_username(db, username=user.username)
    db_user_by_email = get_user_by_email(db, email=user.email)
    if db_user_by_username:
        raise HTTPException(status_code=400, detail="Username already registered")
    if db_user_by_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@router.put("/{user_id}", response_model=UserOut)
def update_existing_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", status_code=204)
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    if not delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
