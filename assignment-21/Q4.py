# Q4. Design python application that creates two threads
# - thread1 should compute sum of elements from a list
# - thread2 should compute product of elements from the list
# - return the result to the main thread and display the results

import threading
def compute_sum(numbers, result, index):
    total = sum(numbers)
    result[index] = total

def compute_product(numbers, result, index):
    product = 1
    for num in numbers:
        product *= num
    result[index] = product

def main():
    numbers = [1, 2, 3, 4, 5]
    result = [0, 0]  # To store sum and product

    thread1 = threading.Thread(target=compute_sum, args=(numbers, result, 0))
    thread2 = threading.Thread(target=compute_product, args=(numbers, result, 1))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"Sum of elements: {result[0]}")
    print(f"Product of elements: {result[1]}")

if __name__ == "__main__":
    main()
