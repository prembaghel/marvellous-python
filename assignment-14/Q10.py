# 8. Write a lambda function which accepts three numbers and return largest number.
largest = lambda a, b, c: a if a > b and a > c else b if b > c else c

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    print("Largest is: ", largest(num1, num2, num3))

if __name__ == "__main__":
    main()
