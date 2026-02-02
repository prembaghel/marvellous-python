# Q5.py Frequency of words in file.
#    - write a program which accepts file name and one string from user and display frequency of that word from file.
import os   

def CountWordFrequency(file_name, word):
    if os.path.exists(file_name):
        with open(file_name, 'r') as fobj:
            content = fobj.read()
            word_count = content.split().count(word)
            print(f"The word '{word}' appears {word_count} times in the file '{file_name}'.")
    else:
        print(f"The file '{file_name}' does not exist in the current directory.")

def main():
    file_name = input("Enter the file name: ")
    word = input("Enter the word to search for: ")
    CountWordFrequency(file_name, word)

if __name__ == "__main__":
    main()
