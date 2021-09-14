"""Will list the programming languages stated below"""
from programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

"""Now create a new list that contains these three existing ProgrammingLanguage objects."""
languages = [ruby, python, visual_basic]
"""Loop through and print the names of all the languages with dynamic typing
(make sure you use your new is_dynamic method!)"""
for language in languages:
    if language.is_dynamic():
        print(language.name)
