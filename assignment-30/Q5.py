# Q5. Find a Word in a File
# Write a Python program that searches for a specific word in a text file. 
# The program should prompt the user to enter the file name and the word to search for, 
# read the file, and display whether the word present in the file or not.

def FindWordInFile(file_name, word_to_search):
    try:
        with open(file_name, 'r') as fobj:
            content = fobj.read()
            if word_to_search in content:
                print(f"The word '{word_to_search}' is present in the file '{file_name}'.")
            else:
                print(f"The word '{word_to_search}' is not present in the file '{file_name}'.")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

def main():
    file_name = input("Enter the file name: ")
    word_to_search = input("Enter the word to search for: ")
    FindWordInFile(file_name, word_to_search)

if __name__ == "__main__":
    main()
