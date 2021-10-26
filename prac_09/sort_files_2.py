"""Let the user categorise different extensions
as the program encounters these, then move them all into those subdirectories"""
import shutil
import os


def main():
    """Sort through files in starting directory and prompt user for a folder
     name based on unique file extensions"""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    extensions = {}

    # Determine folder category for filename extensions
    for file in os.listdir('.'):
        try:
            extension = (file.split('.'))[1]
            extensions[extension]
            pass
        except KeyError:
            valid_answer = False
            while not valid_answer:
                category = input("What category are {} file extensions? ".format(extension))
                if category.isalpha():
                    valid_answer = True
                    extensions[extension] = category
                    try:
                        os.mkdir(category)
                    except FileExistsError:
                        pass
                else:
                    print("Please give a text answer.")

    # Move each file into suitable directory based on its file extension
    for file in os.listdir('.'):
        if os.path.isfile(file):
            file_extension = (file.split('.'))[1]
            file_destination = os.path.join(extensions[file_extension], file)
            print(file_destination)
            shutil.move(file, file_destination)


main()
