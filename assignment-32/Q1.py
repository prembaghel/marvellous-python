# Q1. Design automation script which accepts directory name and display checksum of all files.
#   a. create log file to store names of all files and its checksum.

import os
import sys
import time
import hashlib

def CalculateChecksum(file_path):
    hash = hashlib.md5()
    
    with open(file_path, "rb") as fobj:
        while True:
            buffer = fobj.read(1024)
            if not buffer:
                break
            hash.update(buffer)
    return hash.hexdigest()

def DisplayFilesChecksum(directory):
    try:
        if os.path.exists(directory) is False:
            print(f"The directory '{directory}' does not exist.")
            return

        LogFileName = f"Log_{time.ctime()}.txt"
        fobj = open(LogFileName, 'w')

        files = os.listdir(directory)
        fileCount = 0
        for file in files:
            full_file_name = os.path.join(directory, file)
            if os.path.isfile(full_file_name):
                checksum = CalculateChecksum(full_file_name)
                fileCount += 1
                fobj.write(f"{file}: {checksum}\n")
        fobj.write(f"Total files with checksum in '{directory}': {fileCount}\n")
        fobj.close()

    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")

def main():
    if not len(sys.argv) == 2:
        print("Usage: python Q1.py <directory>")
        return
    directory = sys.argv[1]
    DisplayFilesChecksum(directory)

if __name__ == "__main__":
    main()