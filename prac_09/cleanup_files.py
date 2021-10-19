"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        #Rename file to new name - in place
        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    modified = False
    for character in new_name:
        if character == '_':
            modified = True
            return new_name
    if not modified:
        file_name = []
        for number, character in enumerate(new_name):
            if (character.isupper()) and (number > 0):
                if (new_name[number - 1]).islower():
                    file_name.append(("_{}".format(character)))
                elif (new_name[number - 1]).isupper() and (character.isupper()):
                    file_name.append("_{}".format(character))
            else:
                file_name.append(character)
        file_name = ''.join(file_name)
        return file_name


main()
