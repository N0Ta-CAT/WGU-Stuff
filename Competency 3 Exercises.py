# ---- Math Module --- ##
import math

# Task 1
# use the math module to determine the factorial of the number 7 and print the result
print(math.factorial(7))
# expected outcome: 5040

# Task 2
# use the math module to determine the square root of the number 27 and print the result
print(math.sqrt(27))
# expected outcome: 5.196152422706632

# Task 3
# use the math module to determine the largest integer less than or equal to 15.87 and print the result
print(math.floor(15.87))
# expected outcome: 15

# Task 4
# use the math module to determine the smallest integer integer greater than or equal to 15.87 and print the result
print(math.ceil(15.87))
# expected outcome: 16

# Task 5
# use the math module to determine e to the power of 4
print(math.e ** 4)
# expected outcome: 54.598150033144236

# Task 6
# complete the function that determines the nearest whole number for x and prints the result
def nearest(x):
    print(round(x))
nearest(15.87) #expected result: 16
nearest(7.21) #expected result: 7


# Task 7
# complete the function that determines the square root of x, rounded to the nearest whole number.
def square(x):
    print(round(math.sqrt(x)))

square(38)  # expected result: 6
square(58)  # expected result: 8

## ---- Random Module --- ##
import random

# Task 1
# use the random module to print a random integer between 2 and 20, exclusive
print(random.randrange(2, 20))

# Task 2
# use the random module to print a random number from the range 1 to 100, inclusive
print(random.randrange(1,101))

# Task 3
# use the random module to return a random floating point number
print(random.random())


# Task 4
# Create a list of 6 words. Then use the random module to return a random element from that list.
random_list = ['bee','wasp','spider','ant','fly','ladybug']
print(random.sample(random_list, 1))

## ---- OS Module --- ##
# commented out to test datetime exercises.
import os

# Task 1
# use the os module to create a hard link to C://myfile.txt at C://myPython/myfile.txt
# os.link('C://myfile.txt', 'C://myPython/myfile.txt')

# Task 2
# use the os module to delete the file C://myfile.txt
# os.remove("C://myfile.txt")

# Task 3
# use the os module to return the current working directory
# print(os.getcwd())

# Task 4
# use the os module to change the root directory to C://home/
# os.chdir('C://home/')

## ---- Datetime Module --- ##
import datetime

# Task 1
# use the datetime module to print the current year
print(datetime.datetime.now().year)

# Task 2
# use the datetime module to print the current month
print(datetime.datetime.now().month)

# Task 3
# use the datetime module to print the current day
print(datetime.datetime.now().day)

# Task 4
# use the datetime module to print the total number of seconds in 4 days
# expected outcome: 345600.0
print(datetime.timedelta(days=4).total_seconds())

# Task 5
# print today's date one year from now
print(datetime.datetime.now() + datetime.timedelta(days=365))

# Task 1
# You need to use the datetime library to account for time zone adjustments, but aren't sure which method(s) to use.
# You are taking an exam and can't google it. What Python function will allow you to look up and locate the method?
# Write your code below:
print(help(datetime))

# Task 2
# What built in function would allow me to see ONLY a list of the methods (not the full documentation) associated with a type of object?
#  Call this function on the str data type. Note that you will need to print() the call to this function.
print(help(str))