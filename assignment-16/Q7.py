# Q7. write a program which contains one function that accept one number from user and return true 
# if number is divisible by 5 otherwise return false.
def isDivisibleBy5(num):
    if num % 5 == 0:
        return True
    else:
        return False

def main():
    number = int(input("Enter a number: "))
    if isDivisibleBy5(number):
        print(f"{number} is divisible by 5")
    else:
        print(f"{number} is not divisible by 5")

if __name__ == "__main__":
    main()
