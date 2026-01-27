# Q6. write a program which accepts one number and displays below pattern.
# Input : 5
# Output :
# * * * * *
# * * * *
# * * *
# * *
# *

def display_pattern(n):
    for i in range(n, 0, -1):
        print('* ' * i)

def main():
    number = int(input("Enter a number: "))
    display_pattern(number)

if __name__ == "__main__":
    main()
    