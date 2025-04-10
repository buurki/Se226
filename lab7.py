Task:1
#math_util.py

def add(x,y):
    return x + y
    
def subtract(x,y):
    return x - y
    
def multiply(x,y):
    return x * y
    
def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Error: Zero can not be divisor')

def power(x,y):
    return x ** y

def mod(x,y):
    try:
        return x % y
    except ZeroDivisionError:
        print('Error: Zero can not be divisor')
        
# calculator.py

import math_utils

def main():
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter number.")
        return

    dict = input("Enter operator (+, -, , /, *, %): ")

    dicts = {
        "+": math_utils.add,
        "-": math_utils.subtract,
        "*": math_utils.multiply,
        "/": math_utils.divide,
        "**": math_utils.power,
        "%": math_utils.mod
    }

    func = dicts.get(dict)
    if func is None:
        print("Invalid operator.")
        return

    result = func(x, y)
    if result is None:
        print("Error! Check for division by zero.")
    else:
        print(f"Result: {result}")
if __name__ =="__main__": main()


Task2:
