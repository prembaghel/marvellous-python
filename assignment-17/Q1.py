# Q1. create a module named as arithmetic.py which contains 4 functions as add, subtract, multiply and divide.
# all functions accept two parameters as number and perform the operation and return the result.
# write a python program which imports the module arithmetic and calls all 4 functions by taking user input.


import arithmetic

# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calling functions from arithmetic module
addition = arithmetic.add(num1, num2)
subtraction = arithmetic.subtract(num1, num2)
multiplication = arithmetic.multiply(num1, num2)
division = arithmetic.divide(num1, num2)

# Displaying results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
