# Q1. write a program which contains one lambda function which accespts one parameter and return power of two.
power_of_two = lambda x: x ** 2 
num = int(input("Enter a number: "))
result = power_of_two(num)
print(f"The power of two of {num} is {result}")
