# Q9. write a lambda function using reduce() which accepts list of numbers and returns product of all numbers.
from functools import reduce
data = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, data)
print("Product of all numbers:", product)