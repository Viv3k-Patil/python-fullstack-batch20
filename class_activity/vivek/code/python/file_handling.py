

# file_obj = open("notes2.txt", "w")
# file_obj.write("this is the first statement\n")
# file_obj.write("this is the first statement\n")
# file_obj.write("this is the first statement\n")
# file_obj.write("this is the first statement\n")
# file_obj.write("this is the first statement\n")
# file_obj.write("this is the first statement\n")
# file_obj.write("this is the first statement\n")
# file_obj.write("this is the first statement\n")
# file_obj.close()

# file = open("notes.txt", "w")     # "w" = write mode
# file.write("Hello, this is my first line.\n")
# file.write("This is the second line.\n")
# file.write("this is the first statement\n")
# file.write("this is the first statement\n")
# file.write("this is the first statement\n")
# file.write("this is the first statement\n")
# file.write("this is the first statement\n")
# file.write("this is the first statement\n")
# file.write("this is the first statement\n")
# file.close()                        # ALWAYS close the file when done!

# try:
#     file = open("notes2.txt", "r")
#     print(file.read())
# except FileNotFoundError as e:
#     print(f"file not found, please check the name again")
# finally:
#     file.close()

with open("notes.txt","r") as file:
    print(file.read())


with open("notes.txt", "r") as file:
    print(file.read())          # reads the ENTIRE file as one string

with open("notes.txt", "r") as file:
    print(file.readline())       # reads just ONE line

with open("notes.txt", "r") as file:
    print(file.readlines())       # reads ALL lines into a LIST of strings

with open("notes.txt", "r") as file:
    for line in file:               # loop through the file line by line (memory-efficient!)
        print(line.strip())          # .strip() removes the trailing newline character