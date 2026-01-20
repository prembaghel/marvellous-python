# 2. write a program which contains one function named as ChkGreater() that accepts two numbers from user and display greater number on console.

def ChkGreater():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num1 > num2:
        print("Greater number is:", num1)
    else:
        print("Greater number is:", num2)

ChkGreater()
