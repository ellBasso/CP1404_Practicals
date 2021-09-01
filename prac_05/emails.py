"""
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
Use a separate function to get the name from the email
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        name_confirm = input("Is your name {}? (Y/n) ".format(name))
        if name_confirm.upper() != "Y" and name_confirm != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for address, name in email_to_name.items():
        print("{} ({})".format(name, address))


def get_name_from_email(email_address):
    email_username = email_address.split("@")[0]
    name = " ".join(email_username.split("."))
    return name.title()


main()
