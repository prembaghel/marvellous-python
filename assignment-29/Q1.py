# Q1. Check file exist in current directory.
#    - write a program which accepts file name from user and checks whether the file exists in current directory or not.

import os

def main():
    file_name = input("Enter the file name to check its existence: ")
    if os.path.exists(file_name):
        print(f"The file '{file_name}' exists in the current directory.")
    else:
        print(f"The file '{file_name}' does not exist in the current directory.")

if __name__ == "__main__":
    main()