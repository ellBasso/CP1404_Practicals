from prac_08.silver_service_taxi import SilverServiceTaxi, Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Start of the taxi_simulator script"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0
    print("Lets Drive!")
    print(MENU)
    choice = input("Choice >> ").upper()
    while choice != "Q":
        if choice == "C":
            chosen_taxi = list_taxis(taxis)
        if choice == "D":
            try:
                drive_taxis(taxis, chosen_taxi)
                bill += determine_bill(taxis, chosen_taxi)
            except UnboundLocalError:
                print("Please select a taxi first")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input("Choice >> ").upper()
    list_closing_statement(taxis, bill)


def list_taxis(taxis):
    print("Taxis Available")
    valid_response = False
    while not valid_response:
        for number, taxi in enumerate(taxis):
            print(f"{number} - {taxi}")
        try:
            taxi_choice = int(input("Chose taxi: "))
        except ValueError:
            print("Please enter a valid number")
        try:
            taxi_chosen = taxis[taxi_choice]
            valid_response = True
        except:
            print("Invalid choice")
    print(f"{taxi_chosen.name} Chosen")
    return taxi_choice


def drive_taxis(taxis, chosen_taxi):
    driving_distance = int(input("""How far are we driving?
    >> """))
    taxis[chosen_taxi].drive(driving_distance)


def determine_bill(taxis, chosen_taxi):
    bill = 0
    bill += taxis[chosen_taxi].get_fare()
    print(f"Your {taxis[chosen_taxi].name} trip cost you ${taxis[chosen_taxi].get_fare():.2f}")
    print(f"Your total trip cost ${bill:.2f}")
    return bill


def list_closing_statement(taxis, bill):
    print(f"""Total trip cost: {bill:.2f}
Taxis are now:""")
    for number, taxi in enumerate(taxis):
        print(f"{number} - {taxi}")


main()
