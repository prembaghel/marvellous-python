# Q6. write a lambda function using reduce() which accepts list of numbers and returns the minimum of all numbers.
from functools import reduce
data = [1, 2, 3, 4, 5]
min_num = reduce(lambda x, y: x if x < y else y, data)   
print("Minimum of all numbers:", min_num)