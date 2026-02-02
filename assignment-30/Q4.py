# Q4. Copy Contents of One File to Another
# Write a Python program that copies the contents of one text file to another. 
# The program should prompt the user to enter the source file name and the destination file name, 
# read the contents of the source file, and write them to the destination file.

def CopyFileContents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(content)
        print(f"Contents copied from '{source_file}' to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"The file '{source_file}' does not exist.")

def main():
    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")
    CopyFileContents(source_file, destination_file)

if __name__ == "__main__":
    main()
