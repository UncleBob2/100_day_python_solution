# Display art
from day_14_artwork import logo, vs
import random, os
from day_14_game_data import data

print(logo)

def format_data(account):
    '''Takes the account data and returns the printable format. (defined i/p and o/p'''
    name = account["name"] 
    description = account["description"] 
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    '''Tke the user guess and follower counts and returns if they got it right.'''
    if a_followers > b_followers:
        return guess == "a"
    elif a_followers < b_followers:
        return guess == "b"


score = 0
# generate a random account from the game data

game_over = False
account_b = random.choice(data)

while game_over == False:
    #account A becomes account B
    account_a = account_b

    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct
    # get follower count of each account
    a_follower_num = account_a["follower_count"]
    b_follower_num = account_b["follower_count"]

    # user if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_num, b_follower_num)

    # keep score
    # Give user feedback o their guess
    if is_correct:
        #clear before next question
        os.system('clear')
        print(logo)
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}.")