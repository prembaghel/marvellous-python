# Q4. write a lambda function using reduce() which accepts list of numbers and returns the addition of all numbers.
from functools import reduce

add = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])   
print("Addition of all numbers:", add)