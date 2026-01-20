# 5. write a program which accept one number and checks wheather it is divisible by 3 and 5.
def DivisibleBy3And5(num):
    return (num % 3 == 0 and num % 5 == 0)
        

def DisplayResult():
    num = int(input("Enter a number: "))
    if DivisibleBy3And5(num):
        print(num, "is divisible by 3 and 5.")
    else:
        print(num, "is not divisible by 3 and 5.")

DisplayResult()
