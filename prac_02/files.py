"""
Q1:
Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
"""

user_name = str(input("What is your name? "))
user_name_output_file = 'name.txt'
file_name_output = open(user_name_output_file, 'w')
print(user_name, end="", file=file_name_output)
file_name_output.close()


"""
Q2
Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
"""

user_name_input_file = 'name.txt'
user_name_in_file = open(user_name_input_file, 'r')
read_user_name = user_name_in_file.read()
print("Your name is {}".format(read_user_name))
user_name_in_file.close()


"""
Q3
Create a text file called numbers.txt and save it in your prac_02 directory. Put the following three numbers on separate
lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result,
which should be... 59.
"""

numbers_file = 'numbers.txt'
numbers_file_in = open(numbers_file, 'r')
i = 0
Numbers_Total = 0
while i < 2:
    i += 1
    Numbers_Total += int(numbers_file_in.readline())
print(Numbers_Total)
numbers_file_in.close()


"""
Q4 
Now write a fourth block of code that prints the total for all lines in numbers.txt or a
file with any number of numbers.
"""

file_input = open('numbers.txt', 'r')
print('')
print(file_input.read())
file_input.close()