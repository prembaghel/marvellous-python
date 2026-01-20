# 2. write a program which accepts a number and prints sum of first N natural numbers.

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num + 1):
    sum += i
print(f"Sum of first {num} natural numbers is: {sum}")

