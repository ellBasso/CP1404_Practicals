"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


MENU = """    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""


def display(degrees, unit):
    print("Result: {:.2f} {}".format(degrees, unit))


def fahrenheit_to_celsius_conversion(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def celsius_to_fahrenheit_conversion(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def celsius_to_fahrenheit_input():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius_to_fahrenheit_conversion(celsius)
    display(fahrenheit, "F")


def fahrenheit_to_celsius_input():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = fahrenheit_to_celsius_conversion(fahrenheit)
    display(celsius, "C")


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_to_fahrenheit_input()
        elif choice == "F":
            fahrenheit_to_celsius_input()
        else:
            print("Invalid option")
            print(MENU)
            choice = input(">>> ").upper()
    print("Thank you")


main()
