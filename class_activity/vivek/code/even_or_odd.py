

# take input from user and find out which number is even or odd

# num = int(input("Enter a number: "))

# if num%2 == 0:
#     print('number is even')
# else:
#     print('number is odd')


# a , b and c minimum out of three
# a = 128
# b = 56
# c = 42

# if a < b and a < c:
#     print("a is the smallest")
# elif b < a and b < c:
#     print("b is the smallest")
# else:
#     print("c is the smallest")

# write a function to return area of triangle
# 1/2 * base * height

# def area_of_triangle(base, height):
#     area = 0.5 * base * height
#     return area


# print(area_of_triangle(5, 4))

# find out the missing number sequence in a list

# ls = [11,13,14,15,16,18]

# num = 17

# for each_num in ls:
#     if each_num == num:
#         print(f"number {each_num} is found!!")


# find out the max element in the list

# ls = [11,13,148,8,15,16,18,888]

# # continue, break
# # max, min

# maximum = ls[0]
# minimum = ls[0]

# for num in ls:
#     if maximum < num:
#         maximum = num

#     if minimum > num:
#         minimum = num

# print(maximum)
# print(minimum)

# missing number

# ls = [11,12,13,15,16,17,18]

# idx = 0
# while idx < len(ls) - 1:
#     if (ls[idx + 1] - ls[idx]) == 1:
#         idx += 1
#         continue
#     else:
#         print("missing number is: ", ls[idx]+1)
#         break


# list reverse print 

# ls = [11,12,13,15,16,17,18]
# idx = len(ls) - 1

# while idx >= 0:
#     print(ls[idx])
#     idx = idx - 1

# ls = [11,0,12,0,13,45,0,18,19]
ls = [11,0,12,0,13,45,0,18,19]
# output ls = [11,12,13,45,18,19,0,0,0]


# swap two numbers 
