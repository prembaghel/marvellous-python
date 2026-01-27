# Q4. write a program which accepts number from user and check whether that is positive or negative or zero.
def CheckNumber(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

def main():
    number = int(input("Enter a number: "))
    CheckNumber(number)

if __name__ == "__main__":
    main()
