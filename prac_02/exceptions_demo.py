try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Infinity")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
Questions:

When will a ValueError occur?
 - When the user inputs anything but a number (such as a letter (a) or special character (?) instead of a number like 3 or -3

When will a ZeroDivisionError occur?
 - When the user enters the number 0 as a denominator (as you can't divide by 0 since it will be infinity)

Could you change the code to avoid the possibility of a ZeroDivisionError?
 - Yes, actioned already
If you could figure out the answer to question 3, then make this change now.
"""