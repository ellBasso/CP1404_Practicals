import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Create folders for filename extensions
    for file in os.listdir('.'):
        try:
            os.mkdir((file.split('.'))[1])
            print("Made folder {}".format((file.split('.'))[1]))
        except FileExistsError:
            pass
        except IndexError:
            pass


main()
