# 7. Write a lambda function which accepts one number and return TRUE if number is divisible by 5.
is_divisible_by_5 = lambda x: True if x % 5 == 0 else False

def main():
    num = float(input("Enter a number: "))
    print("Is divisible by 5: ", is_divisible_by_5(num))

if __name__ == "__main__":
    main()
