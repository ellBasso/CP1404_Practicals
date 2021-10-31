"""Create a directory with for each new extension that the program finds"""

import shutil
import os


def main():
    """Set the starting directory and sort through file extensions, create a folder for each type
    then move them into the appropriately named folder based on file extension"""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Create folders for filename extensions
    for file in os.listdir('.'):
        try:
            extension = file.split('.')[1]
            os.mkdir(extension)
            print("Made folder {}".format(extension))
        except FileExistsError:
            pass
        except IndexError:
            pass

    # Move each file into suitable directory based on its file extension
    for file in os.listdir('.'):
        if os.path.isfile(file):
            file_extension = (file.split('.'))[1]
            file_destination = os.path.join(file_extension, file)
            print(file_destination)
            shutil.move(file, file_destination)


main()
