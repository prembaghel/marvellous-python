# 6. Write a lambda function which accepts one number and return TRUE if number is ODD otherwise return FALSE.
is_odd = lambda x: True if x % 2 != 0 else False

def main():
    num = float(input("Enter a number: "))
    print("Is odd: ", is_odd(num))

if __name__ == "__main__":
    main()
