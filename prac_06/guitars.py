"""The program should use a list to store all the user's guitars
(keep inputting until they enter a blank name), then print their details."""

from prac_06.guitar import Guitar


def main():
    guitars = get_guitars()
    show_guitars(guitars)


def get_guitars():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        name = input("Name: ")
    return guitars


def show_guitars(guitars):
    print("These are my guitars:")
    count = 0
    for guitar in guitars:
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {count + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
        count += 1


main()
