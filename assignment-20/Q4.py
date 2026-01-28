# Q4. Design a python application that creates three thread named Small, Capital and Digits.
# - all thread should accept one string as input.   
# - the Small thread should count and display number of lowercase characters.
# - the Capital thread should count and display number of uppercase characters.
# - the Digits thread should count and display number of digits in the string.
# - Each thread must also display
#    - thread ID
#    - thread Name

import threading

def count_lowercase(input_string):
    lowercase_count = sum(1 for char in input_string if char.islower())
    thread = threading.current_thread()
    print(f"[{thread.name}] (ID: {thread.ident}) - Lowercase characters: {lowercase_count}")

def count_uppercase(input_string):
    uppercase_count = sum(1 for char in input_string if char.isupper())
    thread = threading.current_thread()
    print(f"(thread name:{thread.name}) (ID: {thread.ident}) - Uppercase characters: {uppercase_count}")

def count_digits(input_string):
    digit_count = sum(1 for char in input_string if char.isdigit())
    thread = threading.current_thread()
    print(f"(thread name:{thread.name}) (ID: {thread.ident}) - Digits: {digit_count}")

def main():
    input_string = input("Enter a string: ")

    small_thread = threading.Thread(target=count_lowercase, args=(input_string,), name="Small")
    capital_thread = threading.Thread(target=count_uppercase, args=(input_string,), name="Capital")
    digits_thread = threading.Thread(target=count_digits, args=(input_string,), name="Digits")

    small_thread.start()
    capital_thread.start()
    digits_thread.start()

    small_thread.join()
    capital_thread.join()
    digits_thread.join()

    print("Exit from main.")    

if __name__ == "__main__":
    main()