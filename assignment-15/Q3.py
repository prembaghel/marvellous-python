# 3. write a lambda function using filter() which accepts list of numbers and returns list of Odd numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = lambda num: list(filter(lambda x: x % 2 != 0, num))
print("List of odd numbers:", odd_numbers(numbers))
