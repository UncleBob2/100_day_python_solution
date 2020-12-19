import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]


word_list = ["aardvark", "baboon", "camel", "apple"]
chosen_word = random.choice(word_list)

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

lives = 6

display = []

for num_letter in range(len(chosen_word)):
    display += "_"


# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# *** use range for int index instead of 'for letter in chosen_word:
while "_" in display and lives != 0:
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        lives -= 1
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    # print(display) gives ['_', '_', '_', '_', '_']
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    print(stages[lives])
    if "_" not in display:
        print("You win.")
    if lives == 0:
        print("You lose.")

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
