# 1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”

from functools import reduce
str = "1234abcd"
print(str[::-1])

# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12


def countCase(str):
    countLower = 0
    countUpper = 0
    for char in str:
        if char.isupper():
            countUpper += 1
        if char.islower():
            countLower += 1
    print("No. of Uppercase characters : ", countUpper,
          " No. of Lower case Characters : ", countLower)


countCase("abcSdefPghijQkl")


# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

def unique(list):
    uniqueList = []
    for x in list:
        if x not in uniqueList:
            uniqueList.append(x)

    print(uniqueList)


unique([10, 20, 10, 30, 10])


# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.

words = input("Enter hyphen seperated words: ")

result = words.split("-")
result.sort()

final = ("-").join(result)

print(final)

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

str = input("Enter a sequence of lines to capitalize them: ")

upper = str.upper()

print(upper)

# 6. Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.


def add(num1, num2):
    print(int(num1)+int(num2))


num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

add(num1, num2)

# 7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.


def maxLen(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    else:
        print(str1, str2)


maxLen("abcdefgh", "abcdefghi")

# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).

# Tuple is immutable and therefore it can only be a static list and not a dynamic list

# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD


def showNumbers(limit):
    for i in range(limit+1):
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")


showNumbers(3)

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


#even = lambda x: x % 2 == 0


list2 = list(filter(even, list1))

print(list2)

# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#even = lambda x: x % 2 == 0
#square = lambda x: x**2

list2 = list(filter(even, list1))
list3 = list(map(square, list2))

print(list3)

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions


def error():
    try:
        print(5/0)
    except:
        print("An exception occurred")


error()

# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().

li = [1, 2, 3, 4, 5, 6, 7]

red = reduce(lambda a, b: 10*a+b, li)

print(red)

# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.


def multiple(n):
    if n % 3 != 0 and n % 7 == 0:
        print("True")
    else:
        print("False")


multiple(28)

# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.

li = [1, 2, 3, 4]

#m = lambda x : x*x

result = map(m, li)

print(list(result))

# 16. What is the output of the following codes:
# (i) def foo():
# try:
# return 1
# finally:
# return 2
# k = foo()
# print(k)

# nothing

# (ii) def a():
# try:
# f(x, 4)
# finally:
# print('after f')
# print('after f?')
# a()

# after f
# after f?
# Traceback (most recent call last):
#   File "<string>", line 7, in <module>
#   File "<string>", line 3, in a
# NameError: name 'f' is not defined
