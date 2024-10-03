"""Calculator"""
from calculator_art import logo
import os
def clear():
    os.system('cls')
# ########
# #Calculator Start Here# #
def add(num1, num2):
    """Addition"""
    return num1 + num2
# ########

def subtract(num1, num2):
    """Subtraction"""
    return num1 - num2
# ########

def multiply(num1, num2):
    """Multiplication"""
    return num1 * num2
# ########

def divide(num1, num2):
    """Division"""
    return num1 / num2
# ########

def modulo(num1, num2):
    "Modulo"
    return num1 % num2
# ########

def expo(num1, num2):
    "Exponential"
    return num1 ** num2
# ########

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
    "**": expo
}
"Also added  '%' modulo and  '**' exponential"
# ########

" Implementing Code Start Here "
def calculation():
    print(logo)
    num1 = float(input("What is the first number? "))
    for opr in operation:
        print(opr)
    # ########
    
    ask = True
    while ask:
        opr_symbol = input("Pick an operation from above: ")
        num2 = float(input("What is the next number? "))
        calculator = operation[opr_symbol]
        answer = calculator(num1,num2)
        print(f"{num1} {opr_symbol} {num2} = {answer}")
        
        cont = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new program.: ").lower()
        if cont == 'y':
            num1 = answer
        elif cont == 'n':
            clear()
            calculation()
            ask = False
calculation()