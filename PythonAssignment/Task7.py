# 1. Write a program that calculates and prints the value according to the given formula:
# Q = Square root of[(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.

class Calc:
    def __init__(self, D):
        self.D = D

    def calculate(self):
        C = 50
        H = 30
        res = ((2*C*self.D)/H)**0.5
        print(res)


c = Calc(int(input("Enter a value for D: ")))
c.calculate()

# 2. Define a class named Shape and its subclass Square. The Square class has an init function which
# takes length as argument. Both classes have an area function which can print the area of the shape
# where Shape’s area is 0 by default.


class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        print("The area of shape is ", self.length**2)


class Square(Shape):
    def __init(self, length):
        Square.__init__(length)

    def area(self):
        print("The area of the square is ", self.length**2)


s = Square(10)
s.area()

# 3. Create a class to find three elements that sum to zero from a set of n real numbers
# Input array: [-25, -10, -7, -3, 2, 4, 8, 10]
# Expected output: [[-10, 2, 8], [-7, -3, 10]]


class Zero:
    def __init__(self, l):
        self.l = l

    def output(self):
        li = self.l
        res = []
        for i in range(len(li)):
            for j in range(len(li)):
                for k in range(len(li)):
                    if li[i] + li[j] + li[k] == 0:
                        res.append([li[i], li[j], li[k]])
        print(res)


z = Zero([-25, -10, -7, -3, 2, 4, 8, 10])
z.output()

# 4. Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.


class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, hr, mn):
        self.sumHours = hr + self.hours
        self.sumMinutes = mn + self.minutes
        if self.sumMinutes > 60:
            self.sumMinutes -= 60
            self.sumHours += 1

    def displayTime(self):
        print(self.sumHours, " hr and ", self.sumMinutes, " min")

    def displayMinute(self):
        hr = self.sumHours
        mn = self.sumMinutes

        if hr > 0:
            mn = (hr * 60) + mn

        print(mn, "minutes")


t = Time(2, 50)
t.addTime(1, 20)
t.displayTime()
t.displayMinute()

# 5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative
# if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:
# yearPasses() should increase age by the integer value that you are passing inside the function.
# amIOld() should perform the following conditional actions: I
# f age is between 0 and <13, print “You are young”.
# If age is >=13 and <=19, print “You are a teenager”.
# Otherwise, print “You are old”.

# Sample Input for amIOld():
# -1
# 4
# 10
# 16
# 18
# 64
# 38

# Expected Output for amIOld():
# Age is not valid, setting age to 0.
# You are young.
# You are young.
# You are a teenager.
# You are a teenager.
# You are old.
# You are old.

# Consider the age variable to be set to 38 then:
# Sample Input for yearPasses(): 4
# Expected Output for yearPasses(): 42


class Person:
    def __init__(self, age):
        if age >= 0:
            self.age = age
        else:
            self.age = 0
            print("Age is not valid, setting age to 0")

    def yearPasses(self, add):
        self.age += add
        print(self.age)

    def amIOld(self):

        if self.age >= 0 and self.age < 13:
            print("You are young")
        elif(self.age >= 13 and self.age <= 19):
            print("You are a teenager")
        elif self.age > 19:
            print("You are old")


p = Person(38)
p.yearPasses(4)
p.amIOld()
