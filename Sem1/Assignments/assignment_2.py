# 1. Write a Python program to add two numbers with user input.
num1 = int(input("Enter Number 1 :"))
num2 = int(input("Enter Number 2 :"))
sum = print((f"The sum of given two numbers is {num1 + num2}"))

# 2. Write a Python program to find the area of triangle with user input.
a = int(input("Enter First Side of the Triangle : "))
b = int(input("Enter Second Side of the Triangle : "))
c = int(input("Enter Third Side of the Triangle : "))

if (
    a + b > c and b + c > a and c + a > b
):  # Check the given sides are of any triangle or not.
    s = (a + b + c) / 2
    ar = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
    print(f"The area of triangle is for the given sides using Heron's formula is {ar}")
else:
    print(
        f"Given dimensions are not the dimensions of any triangle! Please enter correct sides."
    )

# 3. Write a Python program to swap two user input integer number with using third variable.
a = int(input("Enter the value of a - "))
b = int(input("Enter the value of b - "))

temp = a
a = b
b = temp
print(f"Swapped value of a is {a}")
print(f"Swapped value of b is {b}")

# # 4. Write a Python program to swap two user input integer number without using third variable.
a = int(input("Enter the value of a - "))
b = int(input("Enter the value of b - "))

a = a + b
b = a - b
a = a - b

print(f"Swapped value of a is {a}")
print(f"Swapped value of b is {b}")

# 5. Write a Python program to calculate the average of five user given number.
totalNumbers = int(input("How many numbers of average  you want ? "))
sum = 0
for n in range(totalNumbers):
    num = int(input("Enter the number - "))
    sum += num

print(f"The average of given numbers is {sum/totalNumbers}")

# 6. Write a Python program to generate a random number- i) range 1-10 ii) range 100-500
print("All the numbers between 1 and 10 are ---")
for x in range(2, 10):
    print(x, end=" ")

print(end="\n")

print("All the numbers between 100 and 500 are ---")
for x in range(101, 500):
    print(x, end=" ")


# 7. Write a Python Program to Convert Celsius to Fahrenheit and vice-versa.
#  Celsius to Fahrenheit Formula - fahrenheit = celsius * 1.8 + 32
#  Fahrenheit to Celsius Formula - celsius = (fahrenheit - 32) / 1.8

unit = input(
    'Provide unit in which you want to convert (For Celsius Enter "c" | For Fahrenheit Enter "f") - '
)

if unit == "c":
    tempInF = int(input("Enter your temperature in Fahrenheit : "))
    tempInC = (tempInF - 32) / 1.8
    print(f"Given temperature in Celsius : {tempInC}°C")
else:
    tempInC = int(input("Enter your temperature in Celsius : "))
    tempInF = tempInC * 1.8 + 32
    print(f"Given temperature in Fahrenheit : {tempInF}°F")


# 8. Write a Python Program to Find the Square Root of a positive integer number with user input
print(
    """
**THIS PROGRAM CAN FIND SQAURE ROOT OF ANY POSITIVE INTEGER**
"""
)
num = (int(input("Enter Number : "))) ** (1 / 2)
print("The sqaure root of given number is", num)
