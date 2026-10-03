from app.config import DB_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase



# it know how to connect to the db
engine = create_engine(
    DB_URL,
    echo = True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush= False,
    autocommit = False
)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()