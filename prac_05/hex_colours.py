"""
Use a constant dictionary of about 10 colour names and write a program that allows a user to enter
a name and get the code, e.g. entering AliceBlue (or aliceblue - don't worry about matching the case)
should show #f0f8ff.

Entering an invalid colour name should not crash the program.
Allow the user to enter names until they enter a blank one to stop the loop.
"""
COLOUR_TO_HEX = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "azure1": "#f0ffff",
                 "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000", "blanchedalmond": "#ffebcd",
                 "blue1": "#0000ff", "blueviolet": "#8a2be2", "brown": "#a52a2a"}
print(COLOUR_TO_HEX)

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_TO_HEX:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
