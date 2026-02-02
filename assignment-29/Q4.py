# Q4. Compare two files.
#    - write a program which accepts two file names from command line,
#    - if both file have same content the display SUCCESS otherwise FAILURE.

import os
import sys

def CompareFiles(file1, file2):
    if os.path.exists(file1) and os.path.exists(file2):
        with open(file1, 'r') as fobj1, open(file2, 'r') as fobj2:
            content1 = fobj1.read()
            content2 = fobj2.read()

        if content1 == content2:
            print("SUCCESS: Both files have the same content.")
        else:
            print("FAILURE: The files have different content.")
    else:
        print("One or both files do not exist.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python Q4.py <file1> <file2>")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    CompareFiles(file1, file2)

if __name__ == "__main__":
    main()
