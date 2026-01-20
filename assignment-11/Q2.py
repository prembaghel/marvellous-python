# 2. write a program which accepts a number and prints number of digits in it.

num = int(input("Enter a number: "))

count = 0
while num > 0:
    num = num //10
    print( num)
    count += 1
print(f"Number of digits: {count}")

