print("Welcome to the tip calculator.")
total = float(
    input("What was the total bill? $")
)  # *** REMEMBER TO CONVERT INPUT STRING INTO NUMBER
people = int(input("How many people to split the bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, 15? "))
print("Each person should pay: $", round(total * (1 + (percentage / 100)) / people, 2))
