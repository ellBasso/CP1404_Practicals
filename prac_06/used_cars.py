"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    """1. Create a new Car object called "limo" that is initialised with 100 units of fuel."""
    limo = Car('Limo', 100)

    """2. Add 20 more units of fuel to this new car object using the add method."""
    limo.add_fuel(20)

    """3. Print the amount of fuel in the car."""
    print("Limo has {} units of fuel".format(limo.fuel))

    """4. Attempt to drive the car 115 km using the drive method."""
    limo.drive(115)

    """5. Print the car's odometer reading."""
    print("Limo has driven {}km.".format(limo.odometer))

    """7. add names (literals) to the constructors where you create Car objects in the used_cars.py program."""
    corolla = Car('Corolla', 234540)
    corolla.drive(234480)

    """8. print your car object/s to make sure that the __str__ method is working as expected."""
    print(corolla)
    print(my_car)
    print(limo)


main()
