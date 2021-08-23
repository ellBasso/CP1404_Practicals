numbers = [3, 1, 4, 1, 5, 9, 2]

"""
What values do the following expressions have?

numbers[0] = 3
numbers[-1] = 9
numbers[3] = 1
numbers[:-1] = [3, 1, 4, 1, 5, 9]
numbers[3:4] = [1]
5 in numbers = True
7 in numbers = False
"3" in numbers = False
numbers + [6, 5, 3] = Appends [6, 5, 3] to the end of the list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

"""Change the first element of numbers to "ten" (the string, not the number 10)"""
numbers[0] = "ten"

"""Change the last element of numbers to 1"""
numbers[-1] = 1

"""Get all the elements from numbers except the first two (slice)"""
print(numbers[2:])

"""Check if 9 is an element of numbers"""
if (9 in numbers) is True:
    element_status = "is"
else:
    element_status = "isn't"
print("9 {} an element of numbers".format(element_status))