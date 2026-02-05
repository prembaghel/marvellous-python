# Q3. Design a script which accepts two directory name,'
#   a. copy all files from first directory to second directory.
#   b. second directory should be created if it is not existing.
# python3 Q3.py SourceDir DestDir

import os
import sys
import shutil

def CopyFiles(src_dir, dest_dir):
    try:
        if not os.path.exists(src_dir):
            print(f"The source directory '{src_dir}' does not exist.")
            return

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        files = os.listdir(src_dir)
        for file in files:
            full_file_name = os.path.join(src_dir, file)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dest_dir)

    except Exception as e:
        print(f"Error: {e}")

def main():
    if not len(sys.argv) == 3:
        print("Usage: python Q3.py <source_directory> <destination_directory>")
        return
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    CopyFiles(source_directory, destination_directory)

if __name__ == "__main__":
    main()
