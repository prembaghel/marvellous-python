# 1. Write a lambda function which accepts one number and return its square of that number.
square = lambda x: x * x

def main():
    num = float(input("Enter a number: "))
    print(f"Square of {num} is: {square(num)}")

if __name__ == "__main__":
    main()
