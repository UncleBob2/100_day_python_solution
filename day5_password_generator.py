# Understand the difference between randomizing list and randomizing strings
# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# num_letters = int(
#     input(
#         """
# Welcome to the PyPassword Generator!
# How many letters would you like in your PyPassword?\n"""
#     )
# )
# num_symbols = int(input("How many symbols would you like?\n"))
# num_numbers = int(input("How many numbers would you like?\n"))
num_letters = 12
num_symbols = 2
num_numbers = 2

"""
string = (
    random.choices(symbols, k=num_symbols)
    + random.choices(numbers, k=num_numbers)
    + random.choices(letters, k=num_letters)
)

random.shuffle(string)
print(string)

password = ""
for element in string:
    password += element

print(password)
"""
strings = ""
for letter in range(1, num_letters + 1):
    strings += random.choice(letters)

for num in range(1, num_numbers + 1):
    strings += random.choice(numbers)

for char in range(1, num_symbols + 1):
    strings += random.choice(symbols)

print(strings, "  RAW Password")

x = "".join(random.sample(strings, len(strings)))
print(x, "  Randomized Password using joining string")

pwd1 = ""
pwd2 = ""
pwd3 = ""
# create my own shuffle function
for string in strings:
    part = random.randint(1, 3)
    if part == 1:
        pwd1 += string
    if part == 2:
        pwd2 += string
    if part == 3:
        pwd3 += string

print(pwd3 + pwd1 + pwd2, "  Self developed string shuffle")
