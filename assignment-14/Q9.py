# 8. Write a lambda function which accepts two numbers and return multiplication.
multiplication = lambda a, b: a * b

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Multiplication is: ", multiplication(num1, num2))

if __name__ == "__main__":
    main()
