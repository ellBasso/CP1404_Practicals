"""Crete a taxi names 'Prius 1' and test some of the Taxi class functionality"""

from prac_08.taxi import Taxi

Prius_1 = Taxi("Prius 1", 100)  # Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
Prius_1.drive(40)  # Drive the taxi 40 km
print(Prius_1)  # Print the taxi's details and the current fare
Prius_1.start_fare()  # Restart the meter (start a new fare)
Prius_1.drive(100)  # Drive the car 100 km
print(Prius_1)  # Print the details and the current fare
