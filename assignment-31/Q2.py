# Q2. Design automation script which accepts directory name and two file extension from user.
#   a. rename all file with first file extension to second file extension.
# python3 Q2.py Demo .txt .log

import os
import sys
import time

def RenameFilesWithExtension(directory, old_extension, new_extension):
    try:
        if os.path.exists(directory) is False:
            print(f"The directory '{directory}' does not exist.")
            return

        LogFileName = f"Log_{time.ctime()}.txt"
        fobj = open(LogFileName, 'w')

        files = os.listdir(directory)
        fileCount = 0
        for file in files:
            if file.endswith(old_extension):
                new_file = file.replace(old_extension, new_extension)
                os.rename(os.path.join(directory, file), os.path.join(directory, new_file))
                fileCount += 1
                fobj.write(f"Renamed: {file} to {new_file}\n")
        fobj.write(f"Total files renamed from '{old_extension}' to '{new_extension}': {fileCount}\n")
        fobj.close()

    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")

def main():
    if not len(sys.argv) == 4:
        print("Usage: python Q2.py <directory> <old_extension> <new_extension>")
        return
    directory = sys.argv[1]
    old_extension = sys.argv[2]
    new_extension = sys.argv[3]
    RenameFilesWithExtension(directory, old_extension, new_extension)

if __name__ == "__main__":
    main()
