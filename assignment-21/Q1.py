# Q1. Design a Python application that creates two threads named Prime and NonPrime.
# - Both thread should accept list of integers.
# - the Prime thread should display all the prime numbers from the list.
# - the NonPrime thread should display all the non-prime numbers from the list.

import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def Prime(numbers):
    for n in numbers:
        if is_prime(n):
            print(f"Prime: {n}")

def NonPrime(numbers):
    for n in numbers:
        if not is_prime(n):
            print(f"Non-Prime: {n}")

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    prime_thread = threading.Thread(target=Prime, args=(numbers,))
    non_prime_thread = threading.Thread(target=NonPrime, args=(numbers,))

    prime_thread.start()
    non_prime_thread.start()

    prime_thread.join()
    non_prime_thread.join()

if __name__ == "__main__":
    main()
