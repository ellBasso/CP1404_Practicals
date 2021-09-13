CURRENT_YEAR = 2021
VINTAGE_AGE = 49


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Guitar characteristic variables"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns guitar information in formatted string"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculates the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determines whether the guitar is vintage or not depending on the 'VINTAGE_AGE' constant"""
        if self.get_age() > VINTAGE_AGE:
            return True
