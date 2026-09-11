import re


# a = "My phone number is 9876543210 sdfskdfn 9876543210dnvsldnv  sdjvsjdnvsjk +91(9876543210)"

# print(re.findall(r"\d{10}", a))


text = "My phone number is 9876543210 9876543210 sdfskdfn 9876543210dnvsldnv  sdjvsjdnvsjk +91(9876543210"
match = re.search(r"\d{10}", text)
print(match.group())


import re

text = "Contact us at priya@email.com or rahul@email.com for support."

# findall() — get ALL matching emails
emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)     # ['priya@email.com', 'rahul@email.com']


s = "my credit card no is 1111 1111 11111111 snother credit card no. is 1111111111111111"
pattern1 = r"\d{4}\s?\d{4}\s?\d{4}\s?\d{4}"

print(re.findall(pattern1, s))


text3 = "ABCDE1234E"
pattern2 = r"^[A-Z]{5}\d{4}[A-Z]{1}$"

print(re.findall(pattern2, text3))