from day_10_art import logo
import os


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def div(n1, n2):
    return n1 / n2


def mult(n1, n2):
    return n1 * n2


operations = {"+": add, "-": sub, "*": mult, "/": div}


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")
    # print out some text


def calculator():  # recursion when the function called itself
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    stop_cal = False

    while stop_cal == False:
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")
        continue_cal = input(
            f"Type 'y' to continue to calculate with {answer}, or type 'n' to start a new calculation: "
        )

        if continue_cal == "n":
            stop_cal = True
            screen_clear()
            calculator()
        else:
            num1 = answer


calculator()