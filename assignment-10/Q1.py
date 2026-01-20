# 1. write a program which accepts a number and prints its multiplication table.

num = int(input("Enter a number: "))
print(f"Multiplication table for {num}:")
for i in range(1,11):
    print(num * i)
