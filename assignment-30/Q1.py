# Q1. Count Lines in a File
# Write a Python program that counts the number of lines in a text file. 
# The program should prompt the user to enter the file name, read the file, and display the total number of lines.

def CountLinesInFile(file_name):
    try:
        with open(file_name, 'r') as fobj:
            lines = fobj.readlines()
            print(f"Total number of lines in the file '{file_name}': {len(lines)}")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

def main():
    file_name = input("Enter the file name: ")
    CountLinesInFile(file_name)

if __name__ == "__main__":
    main()
