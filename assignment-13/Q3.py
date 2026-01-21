# 3. write a program which accepts one number and checks whether it is perfect number or not.

def is_perfect_number(num):
    divisors = []   
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num

def main():
    number = int(input("Enter a number: "))
    if is_perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")

if __name__ == "__main__":
    main()
