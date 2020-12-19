# import random


# # test_seed = int(input("Create a seed number: "))
# # random.seed(test_seed)


# names_CSV = input("Give me everybody' names, separated by a comma. ")
# names = names_CSV.split(", ")
# # print(names)

# payer = random.randint(0, len(names) - 1)  # len()-1 else index 0 will suffer X2
# print(payer)
# print(f"{names[payer]} is going to buy the meal today")


# # Nested list

# # dirty_dozen
# fruits = [
#     "Strawberries",
#     "Nectarine",
#     "Apple",
#     "Grapes",
#     "Peaches",
#     "Cherries",
#     "Pears ",
# ]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potates"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)

# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
row_column = list(position)  # This was the break through after thinking
row = int(row_column[0])  # converting string to int
column = int(row_column[1])

map[row - 1][column - 1] = "X"


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")