def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def div(n1, n2):
    return n1 / n2


def mult(n1, n2):
    return n1 + n2


def cal_fun(cal_in, n1, n2):
    cal_in(n1, n2)


operations = {"+": "add", "-": "sub", "*": "mult", "/": "div"}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)

operations_symbol = input("Pick an operation from the lines above: ")


cal = operations[operations_symbol]

answer = cal_fun(cal, num1, num2)


print(f"{num1} {operations_symbol} {num2} = {answer}")