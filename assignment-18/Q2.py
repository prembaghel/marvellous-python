# Q2. write a program which accepts N numbers from user and store them in a list.
# return maximum number from that list.

def max_of_elements(numbers):
    maximum = max(numbers)
    return maximum

def main():
    n = int(input("Enter the number of elements: "))
    numbers = []
    for _ in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)
    print("Maximum element:", max_of_elements(numbers))

if __name__ == "__main__":
    main()
