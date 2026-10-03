from pydantic import BaseModel

# {
#     "name": "department1"
# }

# JSON -> python object -> model -> db

class DepartmentCreate(BaseModel):
    name: str


class DepartmentUpdate(BaseModel):
    name: str