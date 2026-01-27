# Q3. write a program which accepts N numbers from user and store them in a list.
# return minimum number from that list.

def min_of_elements(numbers):
    maximum = min(numbers)
    return maximum

def main():
    n = int(input("Enter the number of elements: "))
    numbers = []
    for _ in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)
    print("Minimum element:", min_of_elements(numbers))

if __name__ == "__main__":
    main()
