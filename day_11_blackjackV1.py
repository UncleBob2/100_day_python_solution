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
    count = 0
    for i in check_cards:
        if i == 11:
            count += 1
    if 11 in check_cards and sum(check_cards) > 21:
        return sum(check_cards) - 10 * count
    else:
        return sum(check_cards)

# 0x9cbb4195bebb36eaa9e4af6272a741a97d7f109a
# ETH-CEL
# USDC-ETH
# USDC-GRT


def blackjack(show_player_cards, show_dealer_cards):
    player_sum = count_card(show_player_cards)
    dealer_sum = count_card(show_dealer_cards)
    if player_sum == 21 or dealer_sum == 21:
        return True
    else:
        return False


def show_card(show_player_cards, show_dealer_cards):
    player_sum = count_card(show_player_cards)
    print(f"Your cards: {show_player_cards}, current score: {player_sum}")
    print(f"Computer's first card: {show_dealer_cards[0]}")


def final_hands(show_player_cards, show_dealer_cards):
    player_sum = count_card(show_player_cards)
    dealer_sum = count_card(show_dealer_cards)
    print(f"Your final hand: {show_player_cards}, final score: {player_sum}")
    print(f"Computer's final hand: {show_dealer_cards}, final score: {dealer_sum}")


run = True
screen_clear()

while run == True:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # cards = [11, 11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10, 11]  # blackjack test

    player_cards = []
    dealer_cards = []
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

    player_sum = 0
    dealer_sum = 0
    stop = False
    blackjack_end = False

    ask_user = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if ask_user == "y":
        screen_clear()
        print(logo)
        show_card(player_cards, dealer_cards)
        blackjack_end = blackjack(player_cards, dealer_cards)
        player_sum = count_card(player_cards)
        while player_sum < 22 and stop == False and blackjack_end == False:
            draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_card == "y":
                player_cards.append(random.choice(cards))
                show_card(player_cards, dealer_cards)
                player_sum = count_card(player_cards)
            elif draw_card == "n":
                stop = True

        dealer_sum = count_card(dealer_cards)
        while dealer_sum < 17 and not dealer_sum > 22 and blackjack_end == False:
            dealer_cards.append(random.choice(cards))
            dealer_sum = count_card(dealer_cards)

        final_hands(player_cards, dealer_cards)
        player_sum = count_card(player_cards)
        dealer_sum = count_card(dealer_cards)
        # print(sum(player_cards), sum(dealer_cards), "blackjack_end = ", blackjack_end)
        if dealer_sum == 21 and blackjack_end == True:
            print("Oppenent Blackjack. Dealer Won.")
        elif player_sum == 21 and blackjack_end == True:
            print("Player Blackjack. Player Won.")
        elif dealer_sum > 21 and player_sum > 21:
            print("You went over. You lose 😤")
        elif dealer_sum < 22 and player_sum > 21:
            print("You went over. You lose 😭")
        elif dealer_sum > 21 and player_sum < 22:
            print("Opponent went over. You win.")
        elif dealer_sum > player_sum:
            print("You lose 😤")
        elif dealer_sum < player_sum:
            print("You win 😃")
        else:
            print("It's a draw. 🙃")
    else:
        run = False


# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
