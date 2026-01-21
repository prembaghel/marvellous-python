# 3. Write a lambda function which accepts two number and return maximum number between them.
maximum = lambda a, b: a if a > b else b

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("maximum is: ",maximum(num1, num2))

if __name__ == "__main__":
    main()
