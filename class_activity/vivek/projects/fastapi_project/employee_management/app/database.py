from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.config import DB_URL

# departments employees
# demodb

# engine -> it knows how to connect to the db
engine = create_engine(
    DB_URL,
    echo = True
)

# session factory
SessionLocal = sessionmaker(
    bind = engine,
    autoflush = False,
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