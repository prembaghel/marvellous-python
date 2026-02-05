# Q1. Design automation script which accepts directory name and file extension from user.
#   a. display all files with given extension.


import os
import sys
import time

def DisplayFilesWithExtension(directory, extension):
    try:
        if os.path.exists(directory) is False:
            print(f"The directory '{directory}' does not exist.")
            return

        LogFileName = f"Log_{time.ctime()}.txt"
        fobj = open(LogFileName, 'w')

        files = os.listdir(directory)
        fileCount = 0
        for file in files:
            if file.endswith(extension):
                fileCount += 1
                fobj.write(file + "\n")
        fobj.write(f"Total files with extension '{extension}': {fileCount}\n")
        fobj.close()

    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")

def main():
    if not len(sys.argv) == 3:
        print("Usage: python Q1.py <directory> <extension>")
        return
    directory = sys.argv[1]
    extension = sys.argv[2]
    DisplayFilesWithExtension(directory, extension)

if __name__ == "__main__":
    main()