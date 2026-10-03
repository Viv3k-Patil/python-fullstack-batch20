from fastapi import FastAPI, Depends
from app.model import Department
from app.database import Base, engine, get_db
from app import model
import psycopg
from sqlalchemy import text, select
from app.config import DB_URL
from app.schema import DepartmentCreate, DepartmentUpdate


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return "hello there!, I'm root"


# @app.get('/departments/raw')
# def get_all_departments_raw():

#     connection = psycopg.connect("postgresql://postgres:password@localhost:5432/demodb")

#     cursor = connection.cursor()

#     cursor.execute(
#         "SELECT * FROM departments"
#     )
#     rows = cursor.fetchall()
#     print(type(rows))
#     print(type(rows[0]))
#     print(rows)

#     cursor.close()
#     connection.close()

#     return rows


# @app.get('/departments/core-text')
# def get_all_departments_core_text(db=Depends(get_db)):
#     result = db.execute(
#         text(
#             "SELECT id, name FROM departments"
#         )
#     )
#     dept = result.mappings().all()
#     print(type(dept[0]))


#     return dept


# @app.get('/departments/core-select')
# def get_all_departments_core_select(db=Depends(get_db)):
#     result = db.execute(
#         select(
#             Department.id,
#             Department.name
#         )
#     ).mappings().all()
#     print(type(result[0]))
#     return result


# get all departments
@app.get('/departments')
def get_all_deparments(db=Depends(get_db)):
    return db.scalars(
        select(Department)
    ).all()

# get department by id
@app.get('/departments/{department_id}')
def get_department_by_id(
    department_id: int,
    db = Depends(get_db)
    ):
    result = db.scalars(
        select(Department).where(Department.id == department_id)
    ).first()
    return result

# create department
@app.post('/departments')
def create_department(new_dept_req: DepartmentCreate, db = Depends(get_db)):
    # create a new model based on user sent attributes
    new_dept = Department(
        name=new_dept_req.name
    )
    db.add(new_dept)
    db.commit()
    db.refresh(new_dept)
    return new_dept

# update department
@app.put('/departments/{dept_id}')
def update_department(
    dept_id:int,
    updated_dept: DepartmentUpdate,
    db = Depends(get_db)
):
    # check if that id present in db, if dept is exists in db
    existing_dept = db.scalars(
        select(Department).where(Department.id == dept_id)
    ).first()

    # if not exists return none
    if existing_dept is None:
        return None

    # if exists, update and commit
    existing_dept.name = updated_dept.name
    db.commit()
    db.refresh(existing_dept)

    # send response to the user
    return existing_dept

# delete department
@app.delete('/departments/{dept_id}')
def delete_department_by_id(
    dept_id: int,
    db = Depends(get_db)
):
    existing_dept = db.scalars(
            select(Department).where(Department.id == dept_id)
        ).first()
    
    # if not exists return none
    if existing_dept is None:
        return None
    
    db.delete(existing_dept)
    db.commit()

    return {
        "message": "deparments deleted successfully!!"
    }


# get all employees
