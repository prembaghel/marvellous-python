# 4. write a program which accepts one number and prints its binary equivalent.
def main():
    number = int(input("Enter a number: "))
    binary_equivalent = bin(number)[2:]
    print(f"Binary equivalent of {number} is: {binary_equivalent}")

if __name__ == "__main__":
    main()
