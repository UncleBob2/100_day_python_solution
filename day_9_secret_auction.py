# www.pythontutor.com
from day_9_logo import logo
import os

print(logo)


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")
    # print out some text


print("Welcome to the secret auction program")
end = False
auction_info = {}

while end == False:
    key = input("What is your name? ")
    value = int(input("what is your bid?: $ "))
    auction_info[key] = value
    condition = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if condition == "no":
        end = True
    else:
        screen_clear()


highest_bid = 0
winner = ""

for person in auction_info:  # no bracket for dictionary
    bid = auction_info[person]
    if bid > highest_bid:
        highest_bid = bid
        winner = person

print(f"The winner is {winner} with a bid of ${highest_bid}")
