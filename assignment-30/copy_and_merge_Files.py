# Q1. copy content from one image file to another file with updated .pdf extension.
# get both file name from command line arguments.
# The program should prompt the user to enter the file name

import os
import sys
from PIL import Image

def copyFileContent(sourceFiles, destinationFile):
    try:
        print(sourceFiles)
        images = [Image.open(file).convert("RGB") for file in sourceFiles]
                
        
        images[0].save(
            destinationFile,
            save_all=True,
            append_images=images[1:]
        )
        print(f"Copied content from '{sourceFiles}' to '{destinationFile}'")

   
    except Exception as e:
        print(f"An error occurred: {e}")
        return

def main():
    
    if len(sys.argv) < 3:
        print("Usage: python test.py <source_file1> [<source_file2> ...] <destination_file>")
        return

    src_files = sys.argv[1:-1]
    destinationFile = sys.argv[-1]

    # call copy function with list of source files and destination filename
    copyFileContent(src_files, destinationFile)
    

if __name__ == "__main__":
    main()
