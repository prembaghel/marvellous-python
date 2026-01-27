# Q4. write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even. 
# Map function will calculate its square. 
# Reduce will return addition of all that numbers.

# example::
# input: [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# list after filter: [2, 4, 4, 2, 8, 10]
# list after map: [4, 16, 16, 4, 64, 100]
# output of reduce: 204


from functools import reduce

def main():
    print("Enter numbers separated by space:")
    numbers = list(map(int, input().split()))

    filtered = list(filter(lambda x: x%2 == 0, numbers))

    mapped = list(map(lambda x: x ** 2, filtered))

    reduced = reduce(lambda x, y: x + y, mapped)

    print("List after filter:", filtered)
    print("List after map:", mapped)
    print("Output of reduce:", reduced)

if __name__ == "__main__":
    main()