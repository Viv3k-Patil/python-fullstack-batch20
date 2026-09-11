

# def greet():
#     print("greet function")

# def greet2():
#     print("greet2 function")


# ls = [greet, greet2]

# for each_function in ls:
#     each_function()

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def calculate(a, b, operation_function):
#     return operation_function(a, b)

# calculate(10, 10, sub)
from datetime import datetime

# decorator
# def my_decorator(func):
#     def wrapper():
#         print(f"this {func} called at {datetime.now()}")
#         print("Something happens BEFORE the function runs 🔵")
#         func()
#         print("Something happens AFTER the function runs 🔴")
#         print(f"this {func} ends at {datetime.now()}")
#     return wrapper

# @my_decorator          # this is EXACTLY equivalent to: say_hello = my_decorator(say_hello)
# def say_hello():
#     print("Hello! 👋")

# say_hello()             # calling say_hello now actually runs the WRAPPED version


# create a function and call throught another

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a/b

# operation_ls = [add, sub, mul, div]

# def cal(a: int, b: int, op: function):
#     return op(a,b)

# print(cal(15, 15, operation_ls[0]))
from datetime import datetime
user = None


def log_decorator(func):
    def wrapper():
        print(f"""
            current logged user: {user}
            current start-time: {datetime.now()}
            current function: {func}
        """)
        func()
        print(f"""
            current logged user: {user}
            current end-time: {datetime.now()}
            current function: {func}
        """)
    return wrapper


def validate_decorator(func):
    def wrapper():
        if user == None:
            print("There is no logged user")
            return
        func()
    return wrapper


@validate_decorator
def greet():
    print("hello world!")


greet()
# @log_decorator
# def add():
#     print(15+20)

# add()


def my_funct():
    print("hello world")

def my_fucntr(a, b):
    print("Sdfsdf")

def my_dfd(a= 0, b=0):
    print("Sdfsd")

def fun_return():
    return "string"

def type_hint_fun(a: int, b: str):
    return 10

def mult_args(*args: int) -> int:
    """"
    vdfsdfbsdfbsfbd
    """
    return sum(args)

def fun_args(some_func: function):
    def sum():
        print(something)
    sum()