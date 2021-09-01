"""
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
Use a separate function to get the name from the email
"""


def main():
    email_directory = {}
    email_address = input("Email: ")
    while email_address != "":
        name = get_name(email_address)
        name_confirm = input("Is your name {}? (Y/n) ".format(name))
        if name_confirm.upper() != "Y" and name_confirm != "":
            name = input("Name: ")
        email_directory[email_address] = name
        email_address = input("Email: ")
    for address, name in email_directory.items():
        print("{} ({})".format(name, address))


def get_name(email_address):
    email_username = email_address.split("@")[0]
    name = " ".join(email_username.split("."))
    return name.title()


main()
