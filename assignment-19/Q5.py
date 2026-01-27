# Q5. write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. 
# Reduce will return maximum of all that numbers.

# example::
# input: [2, 70, 11, 10, 17, 23, 31, 77]
# list after filter: [2, 11, 17, 23, 31]
# list after map: [4, 22, 34, 46, 62]
# output of reduce: 62


from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("Enter numbers separated by space:")
    numbers = list(map(int, input().split()))

    filtered = list(filter(is_prime, numbers))

    mapped = list(map(lambda x: x * 2, filtered))

    reduced = reduce(lambda x, y: x if x > y else y, mapped)

    print("List after filter:", filtered)
    print("List after map:", mapped)
    print("Output of reduce:", reduced)

if __name__ == "__main__":
    main()