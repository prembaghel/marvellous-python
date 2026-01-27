# Q3. write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90. 
# Map function will increase each number by 10. 
# Reduce will return product of all that numbers.

# example::
# input: [4, 34, 36,76, 68, 24, 89, 23, 86, 90, 45, 70]]
# list after filter: [76, 89, 86, 90, 70]
# list after map: [86, 99, 96, 100, 80]
# output of reduce: 6538752000


from functools import reduce

def main():
    print("Enter numbers separated by space:")
    numbers = list(map(int, input().split()))

    filtered = list(filter(lambda x: 70 <= x <= 90, numbers))

    mapped = list(map(lambda x: x + 10, filtered))

    reduced = reduce(lambda x, y: x * y, mapped)

    print("List after filter:", filtered)
    print("List after map:", mapped)
    print("Output of reduce:", reduced)

if __name__ == "__main__":
    main()