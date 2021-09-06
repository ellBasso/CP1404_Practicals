"""
The score must be between 0 and 100 inclusive; 90 or more is excellent; 50 or more is a pass; below 50 is bad.
"""

# for use in the testing function in line 21
import random


def determine_achievement(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def main():
    # score = random.randint(0, 100) # test the system using random variables
    score = float(input("Enter score: "))
    print(determine_achievement(score))


main()
