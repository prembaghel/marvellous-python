# Q3. Design a Python application where multiple threads update a shared variable.
# - use a lock to avoid race conditions
# - Each thread should increment the shared counter multiple times.
# - Display the final value of the counter after all threads have completed their execution.

import threading

def main():
    # Shared variable
    counter = 0
    # Lock for synchronizing access to the shared variable
    lock = threading.Lock()

    # Function to increment the counter
    def increment_counter(num_increments):
        nonlocal counter
        for _ in range(num_increments):
            with lock:
                counter += 1

    
    # Create threads
    threads = []
    for _ in range(7):
        thread = threading.Thread(target=increment_counter, args=(5,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Display the final value of the counter
    print(f"Final counter value: {counter}")

if __name__ == "__main__":
    main()
    

    