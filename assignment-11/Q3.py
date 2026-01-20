# 3. write a program which accepts a number and prints sum of digits.

num = int(input("Enter a number: "))

sum_of_digits = 0
while num > 0:
    sum_of_digits = sum_of_digits + num % 10
    num = num // 10

print(f"Sum of digits: {sum_of_digits}")

