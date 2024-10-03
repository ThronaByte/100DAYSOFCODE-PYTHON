"""Calculator"""
def add(num1, num2):
    """Addition"""
    return num1 + num2

def subtract(num1, num2):
    """Subtraction"""
    return num1 - num2

def multiply(num1, num2):
    """Multiplication"""
    return num1 * num2

def divide(num1, num2):
    """Division"""
    return num1 / num2
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What is the first number? "))
for opr in operation:
    print(opr)
opr_symbol = input("Pick an operation from above: ")
num2 = int(input("What is the second number? "))

# My method
"""if opr_symbol == "+":
    answer = add(num1=num1, num2=num2)

elif opr_symbol == "-":
    answer = subtract(num1=num1, num2=num2)

elif opr_symbol == "*":
    answer = multiply(num1=num1, num2=num2)

elif opr_symbol == "/":
    answer = divide(num1=num1, num2=num2)"""
calculator = operation[opr_symbol]
answer = calculator(num1,num2)
print(f"{num1} {opr_symbol} {num2} = {answer}")

opr_symbol = input("Pick an operation from above: ")
num3 = int(input("What is the second number? "))
calculator = operation[opr_symbol]
answer2 = calculator(answer,num3)
print(f"{answer} {opr_symbol} {num3} = {answer2}")
