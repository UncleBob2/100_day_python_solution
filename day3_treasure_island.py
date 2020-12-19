print(
    """
Welcome to Treasure Island.
Your mission is to find the treasure. """
)
turn = input(
    'You\' are at a cross road. Where do you want to go? Type "left" or "right" \n'
).lower()  # *** NEED TO CONVERT TO LOWER CASES, NEED TO DRAW UP DECISION DIAGRAM
if turn == "left":
    print(
        """You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across."""
    )
    action = input().lower()
    if action == "wait":
        print(
            """You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"""
        )
        option = input().lower()
        if option == "red":
            print("It's a room full of fire. Game Over.")
        elif option == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")

    else:
        print("You get attacked by an angry trout. Game Over")
else:
    print("You fell into a hole. Game Over.")
