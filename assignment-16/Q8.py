# Q4. write a program which accepts number from user and print that numbers of "*" on screen.
def PrintAsterisks(num):
    for i in range(num):
        print("*",  end=" ")
    print()
    
def main():
    number = int(input("Enter a number: "))
    PrintAsterisks(number)

if __name__ == "__main__":
    main()
