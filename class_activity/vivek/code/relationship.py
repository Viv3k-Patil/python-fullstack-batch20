
# student class
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


class Department:
    def __init__(self, dept_name, hod):
        self.dept_name = dept_name
        self.hod = hod
        self.students = []          # a Department HAS students (a list of Student objects)

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print(f"\nStudents in {self.dept_name} Department:")
        for student in self.students:
            print(f"  - {student.name} (Roll No: {student.roll_no})")


class College:
    def __init__(self, college_name):
        self.college_name = college_name
        self.departments = []        # a College HAS departments (a list of Department objects)

    def add_department(self, department):
        self.departments.append(department)

    def show_college_structure(self):
        print(f"🏫 {self.college_name}")
        for dept in self.departments:
            print(f" └── 🏢 {dept.dept_name} (HOD: {dept.hod})")
            for student in dept.students:
                print(f"      └── 🧑‍🎓 {student.name} (Roll No: {student.roll_no})")


abc_college = College("ABC college of engineering")
xyz_college = College("XYZ Technical institute")


cs_dept = Department("Computer Science", "Mr. Tejas")
mech_dept = Department("Mechanical", "Mr. Vivek")

abc_college.add_department(cs_dept)
abc_college.add_department(mech_dept)

suraj = Student("Suraj", 1)
rohit = Student("Rohit", 2)
imran = Student("Imran", 3)

cs_dept.add_student(suraj)
mech_dept.add_student(rohit)
mech_dept.add_student(imran)

abc_college.show_college_structure()