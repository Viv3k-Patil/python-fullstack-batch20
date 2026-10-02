from fastapi import FastAPI, Depends
from app.database import Base, engine, get_db
from app import models
from app.models import Department
from sqlalchemy import select

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return "up and running"


# CRUD for departments

# get all departments
@app.get('/departments')
def get_all_departments(db = Depends(get_db)):
    result = db.scalars(select(Department)).all()
    print(result)

# get department by id

# create department

# update department

# delete department

# CRUD for employees

# get all employees

# get employees by id

# create employees

# update employees

# delete employees