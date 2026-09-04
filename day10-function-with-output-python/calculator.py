# Day10 of 100 days code, python project: calculator with functions and outputs.
logo = """
 🖩 _________

  | 1234567 |
  |---------|
  |[7][8][9]|
  |[4][5][6]|
  |[1][2][3]|
  |[C][0][=]|
  '---------'
"""

print(logo)

import os

def clear():
    """This function here is the screen before another"""
    os.system("cls" if os.name == "nt" else "clear")

def add(n1, n2):
    """Add function to add first to second number"""
    return (n1 + n2)

def multiply(n1, n2):
    """Multiply function to multiply first with second number"""
    return (n1 * n2)

def divide(n1, n2):
    """Divide function to divide first by second number"""
    return (n1 / n2)

def subtract(n1, n2):
    """Subtract function to subtract first number from second number"""
    return (n1 - n2)

operations = {
    "+" : add,
    "*" : multiply,
    "/" : divide,
    "-" : subtract
}

def calculator():
    first_num = float(input("Enter first number: "))
    for symbols in operations:
        print(symbols)
        
    should_continue = True
        
    while should_continue:
        operations_synbols = input("pick your operation: ")
        second_num = float(input("Enter second number: "))
        
        calculator_function = operations[operations_synbols]
        answer = calculator_function(first_num, second_num)
        print(f"{first_num} {operations_synbols} {second_num} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            first_num = answer
        else:
            should_continue = False
            clear()
            calculator()
        
calculator()