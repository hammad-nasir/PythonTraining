# 1. Create three variables in a single line and assign values to them in such a manner that each one of
# them belongs to a different data type.
# E.g. :
# a = 1,
# b = 2.01,
# c = 'string'

a, b, c = 1, 2.01, 'string'

# 2. Create a variable of type complex and swap it with another variable of type integer.

comp = 4j
intNum = 2

intNum = comp

# 3. Swap two numbers using a third variable and do the same task without using any third variable.

var1 = 2
var2 = 4

temp = var1
var1 = var2
var2 = temp

var1 = 2
var2 = 4

var1, var2 = var2, var1

# 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
# Version.

varInput2x = raw_input("Enter a number: ")
varInput3x = input("Enter a number: ")

# print varInput2x
# The above line will work with Python 2x only
print(varInput3x)

# 5. Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.

x = input("Enter a number between 1-10")
y = input("Enter another number between 1-10")
z = x + y
result = z + 30

print(result)

# 6. Write a program to check the data type of the entered values.
# HINT: Printed output should say - The data type of the input value is : int/float/string/etc

checkType = 2.3

print(type(checkType))

# 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
# UPPERCASE.
# (Refer: https://capitalizemytitle.com/camel-case/)

UpperCamelCase = 5
lowerCamelCase = 6.7
snake_case = 3
UPPERCASE = 9

# 8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
# again. Will it change the value? If Yes then Why?

# Yes, variables in Python can be reassigned to variables that have different data types.
