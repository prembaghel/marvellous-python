# Q1. Display file content.
#    - write a program which accepts file name from user, and display file content on console

import os

def main():
    file_name = input("Enter the file name to display its content: ")
    if os.path.exists(file_name):
        fobj = open(file_name, 'r') 
        content = fobj.read()
        print(f"Content of the file '{file_name}':")
        print(content)
    else:
        print(f"The file '{file_name}' does not exist in the current directory.")

if __name__ == "__main__":
    main()