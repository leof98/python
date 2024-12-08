# Day 10 - Calculator project
import art

# Operations functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


print(art.logo)
# Main
def calculator():
    keep_answer = True
    number1 = float(input("What is the first number? "))
    while keep_answer:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        number2 = float(input("What is the next number? "))
        result = operations[operation](number1, number2)
        print(f"{number1} {operation} {number2} = {result}")
        new_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if new_calculation == 'y':
            number1 = result
        else:
            print("\n" * 30)
            keep_answer = False
    calculator()
calculator()
