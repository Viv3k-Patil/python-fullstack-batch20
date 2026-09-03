from functools import wraps
import datetime

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"📝 [{timestamp}] Calling '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"📝 [{timestamp}] '{func.__name__}' finished, returned: {result}")
        return result
    return wrapper

@log_activity
def calculate_total(price, quantity):
    return price * quantity

calculate_total(500, 3)