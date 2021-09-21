from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Ross", "John Johnston", "Jeff Stevens", "Jodie Whittaker"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from dictionary entries and add them to the GUI."""
        for name in self.name_to_phone:
            temp_button = Label(text=name, font_size=48)
            self.root.ids.main.add_widget(temp_button)


DynamicLabels().run()
