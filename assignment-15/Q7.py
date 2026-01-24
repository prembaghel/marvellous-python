# Q7. write a lambda function using filter() which accepts list of string and returns list of strings which have length greater than 5.
strings = ["apple", "banana", "cherry", "date", "elderberry"]

long_strings = list(filter(lambda s: len(s) > 5, strings))
print("Strings with length greater than 5:", long_strings)
