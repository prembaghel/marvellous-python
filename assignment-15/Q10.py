# Q8. write a lambda function using filter() which accepts list of numbers and returns list the count of even numbers.
numbers = [1, 2, 3, 4, 5, 15, 30, 21, 25, 33, 35, 40, 42, 45]

even_numbers_count = len(list(filter(lambda x: x % 2 == 0, numbers)))

print("Count of even numbers:", even_numbers_count)
