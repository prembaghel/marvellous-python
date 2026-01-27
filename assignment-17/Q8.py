# Q8. write a program which accepts one numbers and displays below pattern.
# Input : 5
# Output :
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5 

def display_pattern(n):
    for i in range(n):
        for j in range(1, i + 2):
            print(j, end=' ')
        print()

def main():
    number = int(input("Enter a number: "))
    display_pattern(number)

if __name__ == "__main__":
    main()
