# Q2. write a program which contains one lambda function which accepts two parameters and return its multiplication.
multiply = lambda x, y: x * y
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = multiply(num1, num2)
print(f"The multiplication of {num1} and {num2} is {result}")
