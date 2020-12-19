import random
import os
from day_7_words import word_list
from day_7_art import stages, logo


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")
    # print out some text


# word_list = ["aardvark", "baboon", "camel", "apple"]
chosen_word = random.choice(word_list)

# Testing code
print(logo)
print(f"Pssst, the solution is {chosen_word}.")

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

lives = 6

display = []

for num_letter in range(len(chosen_word)):
    display += "_"


# *** use range for int index instead of 'for letter in chosen_word:
while "_" in display and lives != 0:
    guess = input("Guess a letter: ").lower()
    screen_clear()
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    # print(display) gives ['_', '_', '_', '_', '_']
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")  # ***

    print(stages[lives])
    if "_" not in display:
        print("You win.")
    if lives == 0:
        print("You lose.")
