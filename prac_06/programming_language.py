"""Class for languages.py to use"""


class ProgrammingLanguage:
    """The programming Language class to save the information of programming languages"""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Returns True or False depending on whether the language's typing is dynamic or not"""
        return self.typing == "Dynamic"
