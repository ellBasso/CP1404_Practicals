"""
display menu
get choice
while choice != quit option
    if choice == first option
        do first task
    else if choice == <second option>
        do second task
    ...
    else if choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
do final thing, if needed
"""
choice = ''
while choice != 'Q':
    print("""
    First Option: A
    Second Option: B
    Third Option: C
    Exit/Quit: Q
    """)
    choice = str.upper(input('What is your choice: '))
    if choice == 'A':
        print('First Option Selected')
    elif choice == 'B':
        print('Second Option Selected')
    elif choice == 'C':
        print('Third Option Selected')
    elif choice == 'Q':
        print('Goodbye')
    else:
        print('Invalid Option')