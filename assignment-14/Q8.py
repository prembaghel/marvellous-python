# 8. Write a lambda function which accepts two numbers and return addition.
addition = lambda a, b: a + b

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Addition is: ", addition(num1, num2))

if __name__ == "__main__":
    main()
