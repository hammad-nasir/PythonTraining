# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError

try:
    print("This line has no error")
    print "This line has syntax error"
except:
    print("there is an error in the above line")

# 2. Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.

from sys import argv

script = argv

filename = input("Enter a filename to open: ")

txt = open(filename, 'r')

try:
    txt = open(filename, 'r')
except ValueError:
    filename = input("Enter the correct filename to open: ")


# 3. Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”

while True:
    try:
        num = input("Please enter four digits: ")
        if len(num) == 4:
            break
        else:
            raise TypeError
    except TypeError:
        print("Enter four digits only.")
        continue


# 4. Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.

username = input("Enter your username: ")
password = input("Enter your password: ")
password_again = input("Re-type your password: ")

for i in range(3):
    if password != password_again:
        password_again = input("Incorrect password! Re-type your password: ")
    else:
        print("Login successful!")
        break

# 5. Go through the link provided below to understand finally and raise concept:
# https://www.programiz.com/python-programming/exception-handling

# Done

# 6. Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.

with open("doc.txt", 'r') as f:
    lines = f.readlines()

for line in lines:
    if (len(line)-1) % 2 == 0:
        print(line, end="")
    else:
        print("")
