

def greet():
    print("I'm inside greet function")

def greet2(name):
    print(f"good morning!!, {name}")

def add(x, y):
    # addition
    print(x+y)

def greet3(name = "User"):
    print(f"welcome to the future!!, {name}")

def add_numbers(x, y):
    return x + y


def function1():
    print("start of function 1")
    function2()
    print("end of function 1")

def function2():
    print("start of function 2")
    function3()
    print("end of function 2")

def function3():
    print("inside function 3")
    

x = 10
y = function2
print(x)
print(y)