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

    # Move each file into suitable directory based on its file extension
    for file in os.listdir('.'):
        if os.path.isfile(file):
            file_extension = (file.split('.'))[1]
            file_destination = os.path.join(file_extension, file)
            print(file_destination)
            shutil.move(file, file_destination)


main()
