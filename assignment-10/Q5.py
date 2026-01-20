# 5. write a program which accepts a number and prints all odd numbers till that number.

num = int(input("Enter a number: "))
print(f"Odd numbers till {num}:")
for i in range(1, num + 1):
    if i % 2 != 0:
        print(i)

