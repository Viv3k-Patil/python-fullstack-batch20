
# name = "Python fullstack batch 20"
# technology = "python", "fastapi", "sql"
# students = "a", "b", "c"

# name1 = "Python fullstack batch 21"
# technology1 = "python", "fastapi", "sql"
# students1 = "a", "b", "c"

# batch20 = {
#     "batch_name": "Python fullstack batch 20",
#     "technology": ["python", "fastapi", "sql"],
#     "students": ["a", "b", "c"]
# }

# emp_268897 = {
#     "employee_name": "Mr. John Doe",
#     "designation": "sr. software engineer",
#     "tech-stack": [
#         "python",
#         "fastapi",
#         "django",
#         "java",
#         "springboot",
#         "genai"
#     ]
# } 


# my_list = [12, True, "string", 3.99]
# print(my_list)
# print(type(my_list))

# fruits = ["apple", "banana", "cherry", "banana"]
# print(fruits)

# fruits[0] = "mango" # replace
# fruits.append(56) # insert at the end
# fruits.insert(1, "grapes") #insert at specific index/position
# fruits.extend(["kiwi", "fig"]) 
# print()


# fruits.remove("banana")     # removes the FIRST matching value
# print(fruits)                # ['apple', 'cherry', 'banana']

# popped = fruits.pop()        # removes and returns the LAST item
# print(popped, fruits)        # banana ['apple', 'cherry']

# del fruits[0]                 # removes item at a specific index
# print(fruits)                 # ['cherry']

# fruits.clear()                 # empties the entire list
# print(fruits) 

fruits = ["apple", "banana", "cherry", "banana"]

for each_item in fruits:
    print(each_item)

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

my_str = "Vivek Patil"

for c in my_str:
    print(c)