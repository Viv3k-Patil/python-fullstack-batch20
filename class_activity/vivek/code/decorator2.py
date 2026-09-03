

def greet():
    print("inside greet function")


def outer_func():

    # implement inner function
    def inner_func():
        print("inner function")

    # return inner function
    return inner_func

outer_func()()

ls = [outer_func]


def add(a, b):
    return a+b

add(10,10)


    


