

print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("Before the error")

try:
    result = 10 / 0
except:
    print("cannot divide by zero")

try:
    int("abc")
except Exception:
    print("wrong type")
    
print("After the error") 
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
