# Q3. write program which accepts one number from user and return its factorial.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n):
            n = n * i
        return n
    
def main():
    number = int(input("Enter a number to find its factorial: "))
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
    
if __name__ == "__main__":
    main()