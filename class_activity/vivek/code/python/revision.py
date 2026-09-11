

# a = 10
# b = 10.99
# c = True
# d = 'string'

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# lucky_num = input("Enter your lucky number: ")


# print(8 < 5 and 8 > 3)

# a = int(input("Enter first number: "))
# b = int(input("enter 2nd number: "))


# today = "Tuesday"

# if curr_day == "Monday":
#     print("today is Monday")
# elif curr_day =='Tuesday':
#     print("today is Monday")




# input_string = "smash hulk"

# split_list = input_string.split(" ")
# split_list.sort()


# print(" ".join(split_list))
# name = "Vivek"
# designation = "software engineer"

# print(f"""
#     The candidate name is {name}
#     his designation is {designation}

# """)


# my_list = [12,23,45,78,9,"vivek"]
# my_tuple = (12,4,6,8,4,8,4)
# my_set = {1,2,3,4,5,6,6,7}

# print(my_set)
# for i in my_tuple:
#     print(i)


class Book:

    # constructor
    def __init__(self):
        self.book_name = ''
        self.author = ''
        self.isbn = ''
        self.price = 0
        self.is_available = False

    # actions
    def display_info(self):
        print(f"""
            book name: {self.book_name}
            author: {self.author}
            isbn: {self.isbn}
            price: {self.price}
            is available: {self.is_available}
        """)

    def get_author_name(self):
        print(f"Author name is {self.author}")

# first book object
first_book = Book()
first_book.book_name = 'Attitude is everything'
first_book.author = 'Jeff Keller'
first_book.isbn = 'sdfasdfavdasdvs23dv1sd5'
first_book.price = 299
first_book.is_available = True

sec_book = Book()
sec_book.book_name = 'The brief history of humankind'
sec_book.author = 'Yuhan Harari'
sec_book.isbn = 'sdfasdfavdasdvs23dv1sd5'
sec_book.price = 599
sec_book.is_available = True


first_book.display_info()
sec_book.display_info()

