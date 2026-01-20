# 1. write a program which accepts a number and checks whether it is prime or not.

import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
#print(int(num**0.5) )
#print(int(math.sqrt(num)) )
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
