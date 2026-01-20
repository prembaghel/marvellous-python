# 3. write a program which accept one number and prints square of that number.
def Square(num):
    return num * num

def DisplaySquare():
    num = int(input("Enter a number: "))
    print("Square of", num, "is", Square(num))

DisplaySquare()
