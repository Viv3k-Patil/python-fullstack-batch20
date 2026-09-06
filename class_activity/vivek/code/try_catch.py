try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except TypeError:
    print("❌ That's not a valid number!")
except ValueError:
    print("❌ That's not a valid number!")
except ZeroDivisionError as e:
    print("❌ You can't divide by zero!", e)
else:
    print("runnning else block")
finally:
    print("running finally block")