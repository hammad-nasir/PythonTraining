# 1. Create a list of given structure and get the Access list as provided below:
# x = [100, 200, 300, 400, 500, [1, 2, 3, 4, 5, [
#     10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]
# Access list: [1, 2, 3, 4]Access list: [600, 700]
# Access list: [100, 300, 500, 600, 800]
# Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# Access list: [10]
# Access list: []

x = [100, 200, 300, 400, 500, [1, 2, 3, 4, 5, [
    10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]

print(x[5][0:4])
print(x[6:8])
print(x[0::2])
print(x[::-1])
print(x[5][5][0])

# 2. Create a list of thousand numbers using range and xrange and see the difference between each
# other.
# (For reference: https: // www.techbeamers.com/python-xrange-range/)

rangeList = []
xrangeList = []

for i in xrange(1, 1001):
    xrangeList.append(i)

for i in range(1, 1001):
    rangeList.append(i)

# range is much faster than xrange

# 3. How Tuple is beneficial as compared to the list?

# Tuple makes the code safe as in if the code/data does not need to be changed then tuple should be used. It is also much faster than the list.

# 4. Write a program in Python to iterate through the list of numbers in the range of 1, 100 and print
# the number which is divisible by 3 and is a multiple of 2.

for i in range(1, 101):
    if i % 3 == 0 and i % 2 == 0:
        print(i)

# 5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
# string with their index.

# 6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
# string which is having an even length.

vowel = ['a', 'e', 'i', 'o', 'u']
strTest = "Python"
reverse = strTest[::-1]

print(reverse)

for i in range(len(reverse)):
    if reverse[i] in vowel:
        print(reverse[i], "at index: ", i)

# 7. Write a program in python to print the pair of numbers whose sum is equal to the result
# number that is let's say 8.
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
result = 8

comp = 0
d = {}

for i in range(len(x)):
    comp = result - x[i]
    if x[i] in d:
        print([d[x[i]], x[i]])
    else:
        d[comp] = x[i]

# 8. Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list
# Ask user to enter a number in the range of 1, 50 and make sure if the entered number is
# even, append it to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you enter all the 5 elements, calculate the sum of the list and return the
# maximum of the list.

even_list = []
odd_list = []
maxEven = 0
maxOdd = 0
sumEven = 0
sumOdd = 0

while True:
    num = int(input("Enter a number between 1 and 50: "))
    if num % 2 == 0 and len(even_list) != 5:
        even_list.append(num)
        maxEven = max(num, maxEven)
        sumEven += num
    elif num % 2 != 0 and len(odd_list) != 5:
        odd_list.append(num)
        maxOdd = max(num, maxOdd)
        sumOdd += num
    if len(even_list) == 5 and len(odd_list) == 5:
        break

print("Maximum of even list: ", maxEven)
print("Maximum of odd list: ", maxOdd)
print("Sum of even list: ", sumEven)
print("Sum of odd list: ", sumOdd)


# 9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
# Sample input: 12abcbacbaba344ab
# Expected output: a = 5 b = 5 c = 2
# NOTE: Make sure to avoid counting the occurrence of numeric values in the string.

alphaNum = "12abcbacbaba344ab"
d = {}

for char in alphaNum:
    if char.isnumeric():
        continue
    if char in d:
        d[char] = d[char]+1
    else:
        d[char] = 1

for item in d:
    print(item, " = ", d[item])

# 10. Generate and print another tuple whose values are even numbers in the given tuple
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10).

tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tup2 = tuple(filter(lambda x: x % 2 == 0, tup1))

print(tup2)
