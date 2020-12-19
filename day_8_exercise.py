import math


def greet(name, location):
    print(f"Hello {name}!")
    print(f"you are from {location}.")


# argument provides data where parameters are variables that hold data
# greet("Briston", "Angela")  # positional arguments
# greet(name="Angela", location="Briston")  # keyword arguments


# Write your code below this line 👇


# def paint_calc(height, width, cover):
#     num_of_cans = math.ceil(height * width / cover)
#     print(f"You'll need {num_of_cans} cans of paint.")


# # Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

import math

# Write your code below this line 👇


def prime_checker(number):
    test_limit = math.ceil(math.sqrt(number))

    for i in range(2, test_limit + 1):
        if number == 2:
            print(number, " is a prime number.")
            break
        elif number % i == 0:
            print(number, "is NOT a prime number.")
            break
        elif i >= test_limit:
            print(number, " is a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)