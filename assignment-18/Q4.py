# Q4. write a program which accepts N numbers from user and store them in a list.
# accept one another number from user and return frequency of that number from list.

def frequency_of_number(numbers, target):
    return numbers.count(target)

def main():
    n = int(input("Enter the number of elements: "))
    numbers = []
    for _ in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)
    target = int(input("Enter the number to find frequency: "))
    print("Frequency of", target, "is:", frequency_of_number(numbers, target))

if __name__ == "__main__":
    main()
