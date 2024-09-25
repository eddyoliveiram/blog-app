from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/blog_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_db_connection():
    try:
        db = SessionLocal()
        result = db.execute(text("SELECT 1"))
        print("Conexão com o banco de dados bem-sucedida!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_db_connection()
