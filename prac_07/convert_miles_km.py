from kivy.app import App
from kivy.lang import Builder

MILES_CONVERSION = 1.60934


class MilesConverter(App):
    def build(self):
        """Create box layout window"""
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles(self):
        """Converts the miles value entered to kilometers"""
        self.root.ids.conversion_label.text = str(self.get_valid_miles() * MILES_CONVERSION)

    def handle_increment(self, incr):
        increment = int(incr)
        self.root.ids.miles_input.text = str(self.get_valid_miles() + increment)
        self.convert_miles()

    def get_valid_miles(self):
        """Validates the miles value inputted"""
        try:
            miles = float(self.root.ids.miles_input.text)
            return miles
        except ValueError:
            return 0


MilesConverter().run()
