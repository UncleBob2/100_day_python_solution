import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choices = [rock, paper, scissors]  # 0, 1, 2

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")

user = int(input())  # forgot about convert input into int

print(choices[user])

print("Computer chose:")
computer = int(random.randint(0, 2))
print(choices[computer])

# rock beats scissors, scissors beats paper, paper beats rock, draw
if user == 0 and computer == 2:
    print("You win!")
elif user == 0 and computer == 1:
    print("You lose")
elif user == 1 and computer == 0:
    print("You win")
elif user == 1 and computer == 2:
    print("You lose")
elif user == 2 and computer == 1:
    print("You win")
elif user == 2 and computer == 0:
    print("You lose")
else:
    print("It's a draw")
