from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import SessionLocal
from app.models import User

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/test_db")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"message": "Conexão com o banco de dados bem-sucedida!"}
    except Exception as e:
        return {"message": f"Erro ao conectar ao banco de dados: {e}"}

@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users