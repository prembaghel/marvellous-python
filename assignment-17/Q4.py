# Q4. write a program which accepts one number from user and return addition of its factor.
def sum_of_factors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            print(i)
            total += i
    return total

def main():
    number = int(input("Enter a number to find the sum of its factors: "))
    result = sum_of_factors(number)
    print(f"The sum of factors of {number} is {result}")

if __name__ == "__main__":
    main()