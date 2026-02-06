from sqlalchemy import create_engine  
from sqlalchemy.orm import declarative_base  
from sqlalchemy.orm import sessionmaker  
  
# Base de datos SQLite (archivo local)  
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"  
  
engine = create_engine(  
    SQLALCHEMY_DATABASE_URL,   
    connect_args={"check_same_thread": False}  
)  
  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  
  
Base = declarative_base()  
  
# Dependencia para obtener sesión de BD  
def get_db():  
    db = SessionLocal()  
    try:  
        yield db  
    finally:  
        db.close()