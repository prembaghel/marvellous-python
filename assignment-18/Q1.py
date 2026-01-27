# Q1. write a program which accepts N numbers from user and store them in a list.
# return addition of all elements from that list.
def sum_of_elements(numbers):
    total = sum(numbers)
    return total

def main():
    n = int(input("Enter the number of elements: "))
    numbers = []
    for _ in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)
    print("Sum of elements:", sum_of_elements(numbers))

if __name__ == "__main__":
    main()
