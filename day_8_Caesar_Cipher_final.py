
import day_8_art
import string


num_sym = list(string.digits + string.punctuation + " ")


alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]



def caesar_1(plain_text, shift_amount, direction_code):
    code_text = ""
    shift_amount %= 25  # ensure program still work when shift is greater than alphabet
    if direction == "decode":
        shift_amount *= -1  # ***must be outside of for loop
    for letter in plain_text:
        if letter in num_sym:
            code_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            code_text += alphabet[new_position]
    print(f"Here's is the {direction_code}d results: {code_text}")

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


print(day_8_art.logo)
run_again = True

while run_again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_1(text, shift, direction)
    ask = input("Type 'yes' if you want to run again. Otherwise type 'no'. \n")
    if ask == "no":
        run_again = False
        print("Goodbye")
