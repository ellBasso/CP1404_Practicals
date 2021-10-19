from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Class named SilverServiceTaxi inheriting from Taxi super class"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string content for the class"""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}, " \
               f"{self.current_fare_distance}km on current fare, " \
               f"${self.price_per_km:.2f}/km plus a flagfall of ${self.flagfall:.2f}"
