

def greet():
    yield "hello world 1"
    yield "hello world 2"
    yield "hello world 3"

gen = greet()

print(next(gen))
print(next(gen))
print(next(gen))


def simple_generator():
    print("printing part 1")
    yield 1
    print("printing part 2")
    yield 2
    print("printing part 3")
    yield 3

gen2 = simple_generator()

print(next(gen2))
print(next(gen2))
print(next(gen2))