# Q2. write a program which contains one function names as ChkNum() which accept one parameter as number. 
# if number is even then its should display "Even number" otherwise it should display "Odd number" on console.
def ChkNum(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

def main():
    num = int(input("Enter a number: "))
    ChkNum(num) 

if __name__ == "__main__":
    main()
    