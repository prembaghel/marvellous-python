# Q1. Design python application that creates two saperate threads named as Even and Odd.
# - the Even thread should display first 10 even numbers.
# - the Odd thread should display first 10 odd numbers.
# - both threads should execute independently using Threading module.
# - Ensure proper thread creation and execution.

import threading
import time

def print_even_numbers():
    for i in range(2, 21, 2):
        print("Even:", i)
        time.sleep(1)

def print_odd_numbers():
    for i in range(1, 20, 2):
        print("Odd:", i)
        time.sleep(1)

def main():
    even_thread = threading.Thread(target=print_even_numbers)
    odd_thread = threading.Thread(target=print_odd_numbers)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()


if __name__ == "__main__":
    main()
    print("Both threads have finished execution.")

