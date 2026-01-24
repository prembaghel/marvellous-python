# 2. write a lambda function using filter() which accepts list of numbers and returns list of even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("List of even numbers:", even_numbers)
