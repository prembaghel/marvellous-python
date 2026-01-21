# 2. Write a lambda function which accepts one number and return its cube of that number.
cube = lambda x: x * x * x

def main():
    num = float(input("Enter a number: "))
    print(f"Cube of {num} is: {cube(num)}")

if __name__ == "__main__":
    main()
