import sys

def add(num1, num2):
    add = num1 + num2
    return add

def subtract(num1, num2):
    subtract = num1 - num2
    return subtract

def multiply(num1, num2):
    multiply = num1 * num2
    return multiply

num1 = sys.argv[1]
operation = sys.argv[2]
num2 = sys.argv[3]

if operation == "add":
    output = add(float(num1), float(num2))
    print("Addition:", output)
elif operation == "subtract":
    output = subtract(float(num1), float(num2))
    print("Subtraction:", output)
elif operation == "multiply":
    output = multiply(float(num1), float(num2))
    print("Multiplication:", output)
else:
    print("Unknown operation")

# To run this code in command line
# python 07_Commandlinearg.py 20 add 10
