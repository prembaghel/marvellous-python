# Q4. Design a script which accepts two directory name and a file extension.
#   a. copy specified extension files from first directory to second directory.
#   b. second directory should be created if it is not existing.
# python3 Q4.py SourceDir DestDir .txt

import os
import sys
import shutil
import time

def CopyFiles(src_dir, dest_dir, extension):
    try:
        if not os.path.exists(src_dir):
            print(f"The source directory '{src_dir}' does not exist.")
            return

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        LogFileName = f"Log_{time.ctime()}.txt"
        fobj = open(LogFileName, 'w')
        fileCount = 0
        files = os.listdir(src_dir)
        for file in files:
            full_file_name = os.path.join(src_dir, file)
            if os.path.isfile(full_file_name) and file.endswith(extension):
                shutil.copy(full_file_name, dest_dir)
                fileCount += 1
                fobj.write(f"Copied: {file} to {dest_dir}\n")
        fobj.write(f"Total files copied from '{src_dir}' to '{dest_dir}': {fileCount}\n")
        fobj.close()

    except Exception as e:
        print(f"Error: {e}")

def main():
    if not len(sys.argv) == 4:
        print("Usage: python Q4.py <source_directory> <destination_directory> <file_extension>")
        return
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    extension = sys.argv[3]
    CopyFiles(source_directory, destination_directory, extension)

if __name__ == "__main__":
    main()
