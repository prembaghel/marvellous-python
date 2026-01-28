# Q2. Design a python application that creates two thread named EvenFactor and OddFactor.
# - both thread should accept one integer number as a parameter.
# - the EvenFactor thread should:
#       -identify all even factors of the given number.
#       -calculate and display the sum of even factors.
# - the OddFactor thread should:    
#       -identify all odd factors of the given number.
#       -calculate and display the sum of odd factors.
# - After both thread complete execution, the main thread should display message
#       -"Exit from main."

import threading

def even_factors(number):
    even_factors_list = []
    even_sum = 0
    for i in range(1, number + 1):
        if number % i == 0 and i % 2 == 0:
            even_factors_list.append(i)
            even_sum += i
    print(f"Even factors of {number}: {even_factors_list}")
    print(f"Sum of even factors: {even_sum}")


def odd_factors(number):
    odd_factors_list = []
    odd_sum = 0
    for i in range(1, number + 1):
        if number % i == 0 and i % 2 != 0:
            odd_factors_list.append(i)
            odd_sum += i
    print(f"Odd factors of {number}: {odd_factors_list}")
    print(f"Sum of odd factors: {odd_sum}")


def main():
    number = int(input("Enter an integer number: "))

    even_thread = threading.Thread(target=even_factors, args=(number,))
    odd_thread = threading.Thread(target=odd_factors, args=(number,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main.")

if __name__ == "__main__":
    main()