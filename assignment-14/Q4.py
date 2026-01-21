# 4. Write a lambda function which accepts two number and return minimum number between them.
minimum = lambda a, b: a if a < b else b

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("minimum is: ",minimum(num1, num2))

if __name__ == "__main__":
    main()
