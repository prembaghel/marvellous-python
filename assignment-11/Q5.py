# 5. write a program which accepts a number and checks whether it is palindrome or not.

num = int(input("Enter a number: "))

original_num = num  

def reverse_number(number):
    reversed_num = 0            
    
    while number > 0:
        reversed_num = reversed_num * 10 + number % 10
        number = number // 10

    return reversed_num

reversed_num = reverse_number(num)

is_palindrome = lambda: original_num == reversed_num

if is_palindrome():
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")
    print(f"Reversed number: {reversed_num}")   
