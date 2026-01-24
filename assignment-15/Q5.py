# Q5. write a lambda function using reduce() which accepts list of numbers and returns the maximum of all numbers.
from functools import reduce
data = [1, 2, 3, 4, 5]
max_num = reduce(lambda x, y: x if x > y else y, data)   
print("Maximum of all numbers:", max_num)