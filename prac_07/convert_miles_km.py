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
        """Set the label to predetermined greeting below"""
        miles = float(self.root.ids.miles_input.text)
        self.root.ids.conversion_label.text = str(miles * MILES_CONVERSION)


MilesConverter().run()
