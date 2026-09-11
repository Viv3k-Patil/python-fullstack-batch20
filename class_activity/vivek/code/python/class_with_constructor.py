
class Aadhaar:

    # constructor
    def __init__(self):
        self.name = ""
        self.dob = ""



a = Aadhaar()
a.dob = "11/11/2000"
a.name = "firstname surname"

b = Aadhaar()
b.dob = "9/9/2001"
b.name = "f_name s_name"
print(a)
print(b)