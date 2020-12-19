"""
Don't modify strings.Work with them as lists
>>> s = list("Hello zorld")
>>> s
['H', 'e', 'l', 'l', 'o', ' ', 'z', 'o', 'r', 'l', 'd']
>>> s[6] = 'W'

Turn them into strings only when needed.
>>> s
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
>>> "".join(s)
'Hello World'
"""
"""
0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 	

"""
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


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# # always try to have different the parameters from arguments
# def encrypt(plain_text, shift_amount):
#     cipher_text = [] # solution using list
#     plain_text = list(plain_text)
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_index = position + shift_amount
#         if new_index > 25:
#             new_index -= 25
#         cipher_text.append(alphabet[new_index])

#     print("The encoded text is", "".join(cipher_text))


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""  # solution using string
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")


# def decrypt(plain_text, shift_amount):
#     decipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         decipher_text += alphabet[new_position]
#     print(f"The decrypted text is {decipher_text}")


# def caesar(plain_text, shift_amount, direction_code):
#     code_text = ""
#     out_text = "The coded text is"
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         if direction == "encode":
#             new_position = position + shift_amount
#         else:
#             new_position = position - shift_amount
#             out_text = "The decoded text is"
#         code_text += alphabet[new_position]
#     print(f"{out_text} is {code_text}")


def caesar_1(plain_text, shift_amount, direction_code):
    code_text = ""
    shift_amount %= 26  # ensure program still work when shift is greater than 26
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
