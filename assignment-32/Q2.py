# Q1. Design automation script which accepts directory name and write name of duplicate files in Log file.
#   The script should write names of duplicate files, number of duplicate files in log file.

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

def FindDuplicateFiles(directory):
    try:
        if os.path.exists(directory) is False:
            print(f"The directory '{directory}' does not exist.")
            return
        
        if os.path.isdir(directory) is False:
            print(f"The path '{directory}' is not a directory.")
            return

        LogFileName = f"Log_{time.ctime()}.txt"
        fobj = open(LogFileName, 'w')

        
        Duplicate = {}

        for FolderName, SubFolderName, Filename in os.walk(directory):
            for fname in Filename:
                fname = os.path.join(FolderName,fname)
                Checksum = CalculateChecksum(fname)

                if Checksum in Duplicate:
                    Duplicate[Checksum].append(fname)
                else:
                    Duplicate[Checksum] = [fname]

        for key in Duplicate:
            if len(Duplicate[key]) > 1:
                fileCount = 0
                fobj.write(f"Duplicate files:\n")
                for file in Duplicate[key]:
                    fileCount += 1
                    fobj.write(f"{file}\n")
                fobj.write(f"count:{fileCount}\n")
                fobj.write("\n")

        fobj.close()

    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if not len(sys.argv) == 2:
        print("Usage: python Q1.py <directory>")
        return
    directory = sys.argv[1]
    FindDuplicateFiles(directory)

if __name__ == "__main__":
    main()