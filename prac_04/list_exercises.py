"""
Write a program that prompts the user for 5 numbers and then stores each of these in a list called 'numbers'
"""


def main():
    """Main function to run upon script being ran"""
    if credentials_check() is True:
        numbers = input_numbers()
        number_calculations(numbers)


def input_numbers():
    """Asks the user for the numbers they want to use for later calculations"""
    numbers = []
    count_of_numbers = 5
    for number in range(1, count_of_numbers + 1):
        number_value = int(input("Value for number {}: ".format(number)))
        numbers.append(number_value)
    return numbers


def number_calculations(numbers):
    """Print all of the numerical calculations"""
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format((sum(numbers)) / (len(numbers))))


def credentials_check():
    """Checks to ensure username entered is in the username list"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input(str("Please enter your username: "))
    if username in usernames:
        print("Access Granted")
        return True
    else:
        print("Access Denied")


main()
