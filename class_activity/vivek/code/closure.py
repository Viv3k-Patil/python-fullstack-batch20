

def add(a,b):
    return a+b

add(10,20)
print("end of the program")


def outer_func(greeting: str):
    def inner_func(name):
        print(f"{greeting} {name}")

    return inner_func

a = outer_func("Good morning!!")
a("Vivek")