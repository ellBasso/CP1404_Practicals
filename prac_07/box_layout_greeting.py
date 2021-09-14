from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Create box layout window"""
        self.title = "Greeting program"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Set the label to predetermined greeting below"""
        self.root.ids.greet_label.text = "Hello " + self.root.ids.input_name.text + "!"

    def handle_clear(self):
        """Reset both the text field and the output label to blank"""
        self.root.ids.greet_label.text = "Enter your name"
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
