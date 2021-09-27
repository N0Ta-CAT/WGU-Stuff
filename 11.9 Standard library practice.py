# TASK 1
from math import factorial
def calculate(x):
    x = factorial(x)
    return x

print(calculate(3))  # expected outcome: 6
print(calculate(9))  # expected outcome: 362880

# TASK 2
import random as r
def selection(x):
   return r.sample(x,1)

print(selection(['apple', 'banana', 'orange', 'grape']))
print(selection([7, 5, 3, 9, 12, 4, 8, 10]))

# TASK 3
#Complete the function that takes as input an integer for a number of days
# and prints the total number of seconds in that number of days
import datetime
def currentDate(x):
    td = datetime.timedelta(days=x)
    print('The total number of seconds is ' + str(td.total_seconds()))

currentDate(4) #expected outcome: The total number of seconds is 345600.0.
currentDate(7) #expected outcome: The total number of seconds is 604800.0.

# TASK 4
import datetime as dt
def currentDate():
    initialDate = datetime.date.today()
    formatDate = dt.date.strftime(initialDate, "%m/%d/%Y")
    return 'The current date is ' + formatDate + '.'

print(currentDate())  # Expected outcome will vary, but should follow this format: The current date is 9-11-2018.

# TASK 5
from math import e, ceil
def mathCalculation(x):
    product = x * e
    return ceil(product)

# expected outcome: 9
print(mathCalculation(3))

# expected outcome: 25
print(mathCalculation(9))

# TASK 6
import calendar
# Complete the function to return the number of leap years in the list
def countLeapYears(yearList):
    i = 0
    for year in yearList:
        if calendar.isleap(int(year)):
            i += 1
    return i

# expected output: 2
print(countLeapYears([2001, 2018, 2020, 2090, 2233, 2176, 2200, 2982]))

# expected output: 4
print(countLeapYears([2001, 2018, 2020, 2092, 2204, 2176, 2200, 2982]))

# TASK 7
import calendar
# Complete the function to print the full name of the month using the calendar library
def printMonthName(monthNum):
    monthName = calendar.month_name[monthNum]
    print(monthName)

# expected output: March
printMonthName(3)

# expected output: November
printMonthName(11)

# TASK 8
import calendar, datetime
# Complete the function to print the full name of the day of the week
def printWeekdayName(year, month, day):
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    print days [(.weekday(year,month,day))

# expected output: Friday
printWeekdayName(2001, 8, 31)

# expected output: Monday
printWeekdayName(2018, 10, 1)