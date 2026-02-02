# Q3. Display file Line by Line
# write a program which accepts file name from user and display contents of that file line by line on screen   .
def DisplayFileContentsLineByLine(file_name):
    try:
        with open(file_name, 'r') as fobj:
            for line in fobj:
                print(line, end='')
            print()  # For a new line after file content
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

def main():
    file_name = input("Enter the file name: ")
    DisplayFileContentsLineByLine(file_name)

if __name__ == "__main__":
    main()
