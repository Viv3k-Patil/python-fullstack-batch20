

def calculator_decorator(operation):
    def decorator(func: function):
        def wrapper(a, b):
            print(f"using decorator operation: {operation}")
            return func(a, b)
        return wrapper
    return decorator



@calculator_decorator("addition")
def add(a, b):
    return a+b

print(add(10,10))
