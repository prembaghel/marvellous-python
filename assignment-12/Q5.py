# 5. write a program which accepts a number and prints that many numbers in reverse order.
num = int(input("Enter a number: "))

for i in range(num, 0, -1):
    print(i)