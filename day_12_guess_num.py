import random
from day_12_logo import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS

def check_guess(win_num, user_num):
    if user_num > win_num:
        return "Too High"
    else:
        return "Too Low"

def game():
    # intro
    print(logo)
    print('''Welcome to the Number Guessing Games!\nI'm thinking of a numbr between 1 and 100.''')

    #generate random number from 1 to including 100
    winning_number = random.randrange(1,101)
    correct_guess = False
    num_attempts = set_difficulty()

    while num_attempts >=1 and correct_guess == False:    
        print(f'You have {num_attempts} attempts remaining to guess the number.')    
        # user input number
        guess = int(input("Make a guess: "))
        num_attempts -= 1
        if guess == winning_number:
            print(f'You got it! The answer was {guess}.')
            correct_guess = True
        else:
            print(check_guess(winning_number, guess))
            if num_attempts >= 1:
                print('Guess again.')

    if num_attempts == 0:
        print("You've ran out of guesses, you lose.")

game()

# provide feedback