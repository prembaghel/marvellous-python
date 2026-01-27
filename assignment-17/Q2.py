# Q2. write a program which accespts one number and displays below pattern.
# if user input is 5 then output should be
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *

number = int(input("Enter a number: "))
for i in range(number):
    for j in range(number):
        print("*", end="  ")
    print()
