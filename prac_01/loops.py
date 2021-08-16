"""
displays all of the odd numbers between
1 and 20 with a space between each one.
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print('\n')

"count in 10s from 0 to 100"
for i in range(0, 101, 10):
    print(i, end=' ')
print('\n')

"count down from 20 to 1"
for i in range(20, 0, -1):
    print(i, end=' ')
print('\n')

number_of_stars = int(input("How many stars would you like? "))
for i in range(0, number_of_stars):
    print('*', end='')
print('\n')

for i in range(0, number_of_stars):
    print('*'*(i+1))
print()