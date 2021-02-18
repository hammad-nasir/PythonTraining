# 1. Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
# string.

num1 = 15

if num1 % 3 == 0:
    print("Consultadd")

if num1 % 5 == 0:
    print("Python Training")

if num1 % 5 == 0 and num1 % 3 == 0:
    print("Consultadd - Python Training")

# 2. Write a program in Python to perform the following operator based task:
# -Ask user to choose the following option first:
#     If User Enter 1 - Addition
#     If User Enter 2 - Subtraction
#     If User Enter 3 - Division
#     If User Enter 4 - Multiplication
#     If User Enter 5 - Average

option = int(input("Enter 1 to 5 to perform arithmemtic tasks: "))


# Ask user to enter two numbers and keep those numbers in variables num1 and num2
# respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average as
# soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
# NOTE: At a time a user can only perform one action.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if option == 5:
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))

result = 0

if option == 1:
    result = num1 + num2
elif option == 2:
    result = num1 - num2
elif option == 3:
    result = num1 / num2
elif option == 4:
    result = num1 * num2
else:
    result = (num1+num2+num3+num4)/4

print(result)
if result < 0:
    print("NEGATIVE")

# 3. Write a program in Python to implement the given flowchart:

a = 10
b = 20
c = 30

avg = (a+b+c)/3

print("Avg: ", avg)

if avg > a and avg > b and avg > c:
    print("avergae is higher than a, b and c")
elif avg > a and avg > b:
    print("avg is higher than a and b")
elif avg > a and avg > c:
    print("avg is higher than a and c")
elif avg > b and avg > c:
    print("avg is higher than b and c")
elif avg > a:
    print('avg is just higher than a')
elif avg > b:
    print('avg is just higher than b')
elif avg > c:
    print('avg is just higher than c')


# 4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”

num1 = int(input("enter a number: "))
while(num1):
    if num1 >= 0:
        print("Good Going")
        num1 = int(input("enter a number: "))
        continue
    else:
        print("It's Over")
        break

# 5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200.


for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i)

# 6. What is the output of the following code examples?
# x=123
# for i in x:
#     print(i)
# TypeError: 'int' object is not iterable

#i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
#     else:
#         print("error")
# 0
# error
# 1
# error
# 2

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break

# 0
# 1
# 2
# 3
# 4


# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement

for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    print(i)

# 8. Write a program that accepts a string as an input from the user and calculate the number of digits
# and letters.
# Sample input: consul72
# Expected output: Letters 6 Digits 2

string = input("Enter a string: ")
countAlpha = 0
countNum = 0

for char in string:
    if char.isalpha():
        countAlpha += 1
    elif char.isnumeric():
        countNum += 1

print("Letters ", countAlpha, " Digits ", countNum)

# 9. Read the two parts of the question below:
# Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.
# Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)

luckyNumber = 7

number = int(input("Guess the lucky number: "))
answer = ""

while(number != luckyNumber):
    answer = input("Do you want to continue to guess (yes/no): ")
    if answer == "no":
        break
    else:
        number = int(input("Guess the lucky number: "))


# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as

# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
# The program asks for five guesses(no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.

count = 0
luckyNumber = 7

while(count < 5):
    answer = int(input("Guess the lucky number: "))

    if answer == luckyNumber:
        print("Good guess")
    else:
        print("Try again!")
    count += 1
print("Game over!")


# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
# the while loop so that users do not have to continue guessing after they found the number. If the user
# does not guess the number at all, print “Sorry but that was not very successful”.

count = 0
luckyNumber = 7

while(count < 5):
    answer = int(input("Guess the lucky number: "))
    if answer == luckyNumber:
        print("Good guess")
        break
    else:
        print("Try again!")
    count += 1

if answer != luckyNumber:
    print("Sorry but that was not very successful")
