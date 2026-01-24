# Q8. write a lambda function using filter() which accepts list of numbers and returns list of numbers which is divisible by both 3 and 5.
numbers = [1, 2, 3, 4, 5, 15, 30, 21, 25, 33, 35, 40, 42, 45]
divisible_by_3_and_5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print("Numbers divisible by both 3 and 5:", divisible_by_3_and_5)
