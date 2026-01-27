# Q10. write a program which accepts one number from user return addition of digits in that number.

def sum_of_digits(num):
    if num == 0:
        return 0
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
        
    return sum

def main():
    number = int(input("Enter a number: "))
    print("Sum of digits:", sum_of_digits(number))

if __name__ == "__main__":
    main()
    