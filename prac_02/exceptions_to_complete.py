"""
Get an integer from the user and do not crash when a non-number is entered
"""


finished = False
result = 0
while not finished:
    try:
        result = int(input("Throw me a number: "))
        print("Valid result is:", result)
    except ValueError:
        print("Please enter a valid integer.")
    finished = True

