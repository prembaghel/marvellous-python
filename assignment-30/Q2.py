# Q2. Count Words in a File
# Write a Python program that counts the number of words in a text file. 
# The program should prompt the user to enter the file name, read the file, and display the total number of words.

def CountWordsInFile(file_name):
    try:
        with open(file_name, 'r') as fobj:
            content = fobj.read()
            words = content.split()
            print(f"Total number of words in the file '{file_name}': {len(words)}")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

def main():
    file_name = input("Enter the file name: ")
    CountWordsInFile(file_name)

if __name__ == "__main__":
    main()
