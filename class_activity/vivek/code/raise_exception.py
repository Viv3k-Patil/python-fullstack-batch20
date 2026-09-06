

print("start of the program")

def div(a, b):
    if b < 0:
        raise ZeroDivisionError()
    return a/b



try:
    print(div(5,0))
except:
    print()