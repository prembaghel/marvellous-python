# 4. write a program which accepts a number and prints reverser of that number.

num = int(input("Enter a number: "))
reversed_num = 0            

while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    #print("reversed_num:", reversed_num)
    num = num // 10
    #print("num:", num)

print(f"Reversed number: {reversed_num}")   
