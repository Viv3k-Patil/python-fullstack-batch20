
# # my_list = [1,2,3,4,5]
# # # print(my_list)
# # # print(type(my_list))


# # my_tuple = ("red", "green", "blue")
# # print(my_tuple)
# # print(type(my_tuple))

# # # my_tuple[0] = "purple"
# # print(my_tuple[0:1])

# # # for color in my_tuple:
# # #     print(color)

# # print(list(my_tuple))
# # print(tuple(my_list))


# my_info = {
#     "name": "Vivek",
#     "age": 18,
#     "batch": 20,
#     "skill": "Python"
# }

# print(my_info.keys())
# print(my_info.values())
# print(my_info.items())

# for each in my_info.items():
#     print(each)

# my_info["batch"] = 22
# my_info["location"] = "parihar chowk"
# print(my_info)

# for key, value in my_info.items():
#     print(key, value)

students = {
    "student1": {"name": "Rahul", "age": 21, "marks": [85, 90, 78]},
    "student2": {"name": "Ananya", "age": 22, "marks": [92, 88, 95]}
}

students["student1"]["marks"][0] = 0

student1_info = students["student1"]

student1_marks = student1_info["marks"]

print(students)


my_info = {
    "name": "Vivek",
    "age": 18,
    "batch": 20,
    "skill": ["python", "java"]
}
my_info["skill"][1] = "C++/CPP"
print(my_info)



my_set = {1,2,3,4,5,6}
print(my_set)
print(type(my_set))


fruits = {"apple", "banana", "cherry", "apple", "apple", "apple"}
print(fruits)

print("banana" in fruits)

fruits.add("kiwi")
print(fruits)
# list()
# dict()
# tuple()
# set()

# s = "my name is Shaktiman"
# print(set(s))

for fruit in fruits:
    print(fruit)