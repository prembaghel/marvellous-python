# Q1. Design a Python application that creates two threads
# - the thread 1 should calculate and display maximum number from the list.
# - the thread 2 should calculate and display minimum number from the list.
# - the list should be accepted from user.

import threading

def find_maximum(numbers):
    maximum = max(numbers)
    print(f"Maximum number: {maximum}")

def find_minimum(numbers):
    minimum = min(numbers)
    print(f"Minimum number: {minimum}")

def main():
    numbers = list(map(int, input("Enter a list of numbers (space-separated): ").split()))
    thread1 = threading.Thread(target=find_maximum, args=(numbers,))
    thread2 = threading.Thread(target=find_minimum, args=(numbers,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()