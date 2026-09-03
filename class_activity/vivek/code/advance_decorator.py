
# upper decorator

def upper_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


# exclaim decorator
def explaim_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!"
    return wrapper


@explaim_decorator
@upper_decorator
def greet():
    return "hello world"

print(greet())