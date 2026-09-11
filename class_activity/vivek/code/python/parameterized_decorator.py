

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)

        return wrapper
    return decorator


@repeat(times = 7)
def greet(name):
    print(f"""
        Good morning!!, {name}
    """)

greet("Vivek")

