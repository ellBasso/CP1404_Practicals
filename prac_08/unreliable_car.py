from prac_08.car import Car
import random


class UnreliableCar(Car):
    """derived class for an UnreliableCar that inherits from Car"""

    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance=0):
        """generate a random float number between 0 and 100, and only drive
        the car if that number is less than the car's reliability"""
        if random.uniform(1, 100) <= self.reliability:
            return distance
        return 0
