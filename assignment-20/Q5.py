# Q5. Design a python application that creates two thread named Thread1 and Thread2.
# - Thread1 should display numbers from 1 to 50.
# - Thread2 should display numbers from 50 to 1
# - Ensure that:
#    - thread2 starts execution only after the completion of thread1.
# - use appropriate synchronization.

import threading
import time

def Thread1():
    for i in range(1, 6):
        print(f"Thread1: {i}")
        # time.sleep(0.1)  # Added sleep to simulate work being done

def Thread2():
    for i in range(5, 0, -1):
        print(f"Thread2: {i}")
        # time.sleep(0.1)  # Added sleep to simulate work being done

def main():
    thread1 = threading.Thread(target=Thread1,)
    thread2 = threading.Thread(target=Thread2,)

    thread1.start()
    thread1.join()  # Wait for Thread1 to complete
    
    thread2.start()
    thread2.join()

    print("Exit from main.")

if __name__ == "__main__":
    main()  