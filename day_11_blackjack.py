############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

from day_11_art import logo
import random
import os


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")
    # print out some text


def count_card(check_cards):
    if 11 in check_cards and sum(check_cards) > 21:
        return sum(check_cards) - 10
    else:
        return sum(check_cards)


def show_card(show_player_cards, show_dealer_cards):
    player_sum = count_card(show_player_cards)
    print(f"Your cards: {show_player_cards}, current score: {player_sum}")
    print(f"Computer's first card: {show_dealer_cards}")
    return player_sum


def final_hands(show_player_cards, show_dealer_cards):
    dealer_sum = count_card(show_dealer_cards)
    player_sum = count_card(show_player_cards)
    print(f"Your final hand: {show_player_cards}, final score: {player_sum}")
    print(f"Computer's final hand: {show_dealer_cards}, final score: {dealer_sum}")


while True:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11]
    # screen_clear()
    ask_user = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    player_cards = []
    dealer_cards = []
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

    player_sum = 0
    stop = False
    dealer_sum = 0

    if ask_user == "y":
        print(logo)
        player_sum = show_card(player_cards, dealer_cards)
        while player_sum < 22 and stop == False:
            draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_card == "y":
                player_cards.append(random.choice(cards))
                player_sum = show_card(player_cards, dealer_cards)
            elif draw_card == "n":
                stop = True

        while dealer_sum < 17 and not dealer_sum > 22:
            dealer_cards.append(random.choice(cards))
            dealer_sum = sum(dealer_cards)

        final_hands(player_cards, dealer_cards)
        if dealer_sum > 21 and player_sum > 21:
            print("Both went over. It's a draw")
        elif dealer_sum < 22 and player_sum > 21:
            print("You went over. You lose.")
        elif dealer_sum > 21 and player_sum < 22:
            print("Dealer went over. You win.")
        elif dealer_sum > player_sum:
            print("Dealer is higher. You lose.")
        elif dealer_sum < player_sum:
            print("Player is higher. You win.")
        else:
            print("It's a draw.")


# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
