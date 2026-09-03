

# decorator is a function that takes input as function and return function
# it takes our function and add extra functionality

def my_decorator(func):
    def wrapper(*args, **kwargs):       # accepts any number of positional/keyword arguments
        print("Before the function runs...")
        result = func(*args, **kwargs)    # pass them along to the original function
        print("After the function runs...")
        return result                       # don't forget to return the original result!
    return wrapper

@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

print(add(5, 3))                # Before... 8  After...
greet_user("Priya")              # Before... Hello, Priya!  After...
greet_user("Rahul", greeting="Hi")   # Before... Hi, Rahul!  After...