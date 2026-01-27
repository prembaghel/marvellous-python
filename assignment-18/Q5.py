# Q5. write a program which accepts N numbers from user and store them in a list.
# return addition of all prime numbers from that list. main python file accepts N numbers from user 
# and pass each number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. name of the function from main python file should be ListPrime().

import MarvellousNum

def ListPrime(numbers):
    return [num for num in numbers if MarvellousNum.is_prime(num)]

def main():
    n = int(input("Enter the number of elements: "))
    numbers = []
    for _ in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)
    prime_numbers = ListPrime(numbers)
    print("Prime numbers in the list are:", prime_numbers)
    print("Sum of prime numbers:", sum(prime_numbers))  

if __name__ == "__main__":
    main()
    
