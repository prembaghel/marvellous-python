# 4. write a program which accept one number and prints cube of that number.

def Cube(num):
    return num * num * num

def DisplayCube():
    num = int(input("Enter a number: "))
    print("Cube of", num, "is", Cube(num))

DisplayCube()
