

def add_2_decorator(func: function):
    def wrapper(*args, **kwargs):
        a = func(*args)
        return a + 2
    return wrapper


@add_2_decorator
def get_number(a: int):
    return a

print(get_number(500))