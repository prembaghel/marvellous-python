# Q9. write a program which accepts one number from user return number of digits in that number.
def count_digits(num):
    if num == 0:
        return 1
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

def main():
    number = int(input("Enter a number: "))
    print("Number of digits:", count_digits(number))

if __name__ == "__main__":
    main()
    