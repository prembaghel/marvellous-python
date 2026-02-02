# Q3. Copy file content into new file.
#    - write a program which accepts file name from command line, 
#    - creates a new file named as "Copy_of_<OriginalFileName>" and copies the content of original file into new file.

import os
import sys


def CreateFileCopy(original_file_name):
    if os.path.exists(original_file_name):
        with open(original_file_name, 'r') as fobj:
            content = fobj.read()

        new_file_name = f"Copy_of_{original_file_name}"
        
        with open(new_file_name, 'w') as fobj:
            fobj.write(content)

        print(f"Content copied to new file '{new_file_name}'.")
    else:
        print(f"The file '{original_file_name}' does not exist in the current directory.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Q3.py <file_name>")
        return

    original_file_name = sys.argv[1]
    CreateFileCopy(original_file_name)

if __name__ == "__main__":
    main()
