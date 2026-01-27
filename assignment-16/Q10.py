# Q10. write a program which accepts name from user and display length of its name.
def DisplayNameLength(name):
    length = len(name)
    print(f"Length of the name '{name}' is: {length}")

def main():
    user_name = input("Enter your name: ")
    DisplayNameLength(user_name)

if __name__ == "__main__":
    main()
