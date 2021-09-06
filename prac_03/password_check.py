"""
asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
Example: if the user enters "Pythonista" (10 characters), the program should print "**********".
"""

MINIMUM_PASSWORD_LENGTH = 10


def get_password():
    requested_password = input("What password would you like to set? ")
    return requested_password


def check_password(requested_password):
    if len(requested_password) >= MINIMUM_PASSWORD_LENGTH:
        return True
    else:
        return False


def print_password_stars(accepted_password):
    print('*' * len(accepted_password))
    print("Password check successful.")


def main():
    requested_password = input("What password would you like to set? ")
    while not check_password(requested_password):
        print("Password does not satisfy the required minimum length of {} characters".format(
            MINIMUM_PASSWORD_LENGTH))
        requested_password = input("What password would you like to set? ")
    print_password_stars(requested_password)


main()
