# 1. Create a list of 10 elements of four different data types like int, string, complex and float.

listTen = [2, 3, 5.6, "add", 4.2, 4j, 3.6, "sub", 5, 1.5]

# 2. Create a list of size 5 and execute the slicing structure

numFive = [5, 3, 8, 7, 6]
subNumFive = numFive[1:4]

# 3. Write a program to get the sum and multiply of all the items in a given list.

numFive = [5, 3, 8, 7, 6]
add = 0
multiply = 1

for i in range(len(numFive)):
    add += numFive[i]
    multiply *= numFive[i]

print(add)
print(multiply)

# 4. Find the largest and smallest number from a given list.

numFive = [5, 3, 8, 7, 6]

smallest = min(numFive)
largest = max(numFive)

print(smallest)
print(largest)


# 5. Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list.

numFive = [5, 3, 8, 7, 6]
result = []

for i in range(len(numFive)):
    if numFive[i] % 2 != 0:
        result.append(numFive[i])

print(result)

# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and30(both included).

result = []
for i in range(1, 31):
    if i <= 5 or i >= 26:
        result.append(i**2)
print(result)

# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

list1.pop()
list1 = list1 + list2
print(list1)

# 8. Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a = {1: 10, 2: 20} b = {3: 30, 4: 40}
# Expected output: {1: 10, 2: 20, 3: 30, 4: 40}

a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
a.update(b)
print(a)


# 9. Create a dictionary that contain numbers in the form(x: x*x) where x takes all the values between 1
# and n(both 1 and n included).
# Sample input: n = 5
# Expected output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = 6
dict = {}
for i in range(1, n+1):
    dict[i] = i**2
print(dict)

# 10. Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
# Sample input: 34, 67, 55, 33, 12, 98
# Expected output: [‘34’, ’67’, ’55’, ’33’, ’12’, ’98’](‘34’, ’67’, ’55’, ’33’, ’12’, ’98’

str = input("enter comma seperated numbers: ")

list = str.split(", ")
tuple = tuple(str.split(", "))

print(list, tuple)
