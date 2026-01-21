# 5. Write a lambda function which accepts one number and return TRUE if number is even otherwise return FALSE.
is_even = lambda x: True if x % 2 == 0 else False

def main():
    num = float(input("Enter a number: "))
    print("Is even: ", is_even(num))

if __name__ == "__main__":
    main()
