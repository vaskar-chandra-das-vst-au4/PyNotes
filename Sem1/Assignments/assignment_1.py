# Assignment 1

# # @ Calculate SI ->

# p = int(input("Enter Principal Amount: "))
# t = int(input("Enter time: "))
# r = int(input("Enter rate per annum: "))
# SI = p * r * t / 100
# print("The SI obtained using given data is", SI)


# # @ Greet ->
# userName = input("Enter your name :")
# print("Hello {}".format(userName))


# # @  Addition of given two numbers ->
# firstInt = int(input("Enter first number:"))
# secondInt = int(input("Enter second number:"))
# add = firstInt + secondInt
# print("Addition of given two numbers is {}".format(add))


# # @ Time conversion ->
# seconds = int(input("Enter seconds :"))
# minutes = seconds / 60
# hour = minutes / 60

# print("Hours: {}".format(hour))
# print("Minutes: {}".format(minutes))
# print("Seconds:{}".format(seconds))

# # @ Number swapping ->
# firstNum = int(input("Enter the value of num1:"))
# secondNum = int(input("Enter the value of num2:"))

# switch = firstNum
# firstNum = secondNum
# secondNum = switch
# print("Swapped values - num1 = {} and num2 = {}".format(firstNum, secondNum))

# # @ Find area and circumference of a circle ->
# import math

# r = int(input("Enter radius of the circle:"))
# c = 2 * math.pi * r
# ar = math.pi * r**2
# print(
#     f"The area and the circumference, calculated using the radius = {r} units are {ar} units sq and {c} units."
# )
# # @ CI ->
# p = int(input("Enter Principal Amount: "))
# t = int(input("Enter time: "))
# r = int(input("Enter rate per annum: "))
# CI = p * (1 + r / 100) ** t - p
# print("The CI obtained using given data is", CI)


# # ~ Date and time ->
import datetime

now = datetime.datetime.now()
date = now.strftime("%B %d %Y")
time = now.strftime("%H:%M:%S")

print("Date + Time -", now)
print("Date -", date)
print("Time -", time)

date = now.strftime("%d/%b/%Y")
print("Date -", date)
date = now.strftime("%d/%B/%Y")
print("Date -", date)
date = now.strftime("%d/%m/%y")
print("Date -", date)


# ~ Import calender
import calendar

year = int(input("Enter year:"))
month = int(input("Enter month:"))

print("Calender of given year and month  -")
print(calendar.month(year, month))
