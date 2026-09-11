import json

# Writing a Python dictionary to a JSON file
student = {"name": "Priya", "age": 21, "course": "Python Full Stack"}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)     # indent=4 makes it nicely formatted/readable


# Reading a JSON file back into a Python dictionary
with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])       # Priya
print(type(data))   