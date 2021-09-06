"""
asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.

These values should be stored as CONSTANTS

Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
"""

import random

MIN = 1
MAX = 45
NUMBERS_PER_LINE = 6


def main():
    """Runs program"""
    quick_pick_count = int(input("Number of quick picks to generate: "))
    for line_count in range(1, quick_pick_count + 1):
        numbers_in_line = []
        for number in range(1, NUMBERS_PER_LINE + 1):
            random_number = random.randint(MIN, MAX)
            while random_number in numbers_in_line:
                random_number = random.randint(MIN, MAX)
            numbers_in_line.append(random_number)
        numbers_in_line.sort()
        print(" ".join("{:2}".format(number) for number in numbers_in_line))


main()
