# Q3. Design a python application that creates two thread named EvenList and OddList
# - both thread should accept list of integers as input.
# - the EvenList thread should:
#       -extract all even elements from the given list.
#       -calculate and display their sum.
# - the OddList thread should:
#       -extract all odd elements from the given list.
#       -calculate and display their sum.
# - threads should run concurrently.

import threading

def EvenList(numbers):
    even_list = [num for num in numbers if num % 2 == 0]
    even_sum = sum(even_list)
    print(f"Even elements: {even_list}")
    print(f"Sum of even elements: {even_sum}")


def OddList(numbers):
    odd_list = [num for num in numbers if num % 2 != 0]
    odd_sum = sum(odd_list)
    print(f"Odd elements: {odd_list}")
    print(f"Sum of odd elements: {odd_sum}")


def main():
    numbers = [int(x) for x in input("Enter a list of integers (space-separated): ").split()]

    even_thread = threading.Thread(target=EvenList, args=(numbers,))
    odd_thread = threading.Thread(target=OddList, args=(numbers,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main.")

if __name__ == "__main__":
    main()
         