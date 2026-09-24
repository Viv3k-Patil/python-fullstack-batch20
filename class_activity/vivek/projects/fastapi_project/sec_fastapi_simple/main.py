from fastapi import FastAPI

app = FastAPI()

students = {
    1: {"name": "Rahul", "age": 20, "grade": "A"},
    2: {"name": "Priya", "age": 21, "grade": "B+"},
    3: {"name": "Amit", "age": 19, "grade": "A-"},
    4: {"name": "Sneha", "age": 20, "grade": "B"},
    5: {"name": "Arjun", "age": 22, "grade": "A+"}
}

@app.get('/health')
def check_health():
    return {
        "health": "OK"
    }

@app.get('/root')
def check_health():
    return {
        "path": "root"
    }

# get all students
@app.get('/students')
def get_all_students():
    return {
        "students": students
    }

# get student by id
# 2 -> Yogita
# /students/2
@app.get('/students/{student_id}')
def get_student_by_id(student_id: int):
    return {
        "student": students[student_id]
    }

# query parameter
# student_id
# /students?id=2
@app.get('/student')
def get_student(id: int):
    return {
        "id": id,
        "student": students[id]
    }

# add a new student
@app.post('/students')
def create_student(id: int, name:str, age: int, grade: str):
    students[id] = {
        "name": name,
        "age": age,
        "grade": grade
    }
    return {
        "message": "student added successfully"
    }

@app.delete('/students/{student_id}')
def delete_student(student_id: int):
    deleted_student = students.pop(student_id, None)
    print(delete_student)
    return {
        "deleted": "true",
        "deleted_id": student_id
    }