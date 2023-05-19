# 1.The volume of a sphere with radius r is (4/3)*πr3. Write a Python program which accepts the radius of a sphere and computes the volume. What is the volume of a sphere with radius 5?
from math import pi

r = int(input("Enter radius of the sphere : "))
vol = print(f"The volume of the sphere for given radius is {(4/3)*pi*r**3} unit cube.")


# 2. Suppose the cover price of a book is Rs 240.95, but bookstores get a 40% discount. Shipping costs Rs 30 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

# 75 cents  = 0.445145 Rs

# Discounted price of 60 copies excluding shipping cost =  60*240.95*0.6
# Total shipping cost = 30 + 59*0.445145

totalCost = (
    60 * 240.95 * 0.6 + 30 + 59 * 0.445145
)  # Cost of all copies including shipping cost


print(f"The wholesale cost of 60 copies is {totalCost}")


# 3. Write a Python program to find the maximum from a list of number.
randomNumbers = [34, 90, 12, 50, 900, 678]
print("The greatest number in the list is ", max(randomNumbers))
print("The smallest number in the list is ", min(randomNumbers))


# 4. Write a Python program to perform Linear search.present

# A simple approach is to do a linear search, i.e
# Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
# If x matches with an element, return the index.
# If x doesn’t match with any of the elements, return -1.
num = [20, 45, 13, 56, 80, 78, 100, 567, 987]

present = False
for x in num:
    if x == 987:
        print("Index of x in the list is", num.index(x))
        present = True

if present == False:
    print(-1)

# 5. Write a program to check if a number is Odd or even. Take input from user.
print(
    """
**Program to check the provided number is odd or even**
"""
)

inputNum = int(input("Enter number : "))

if inputNum % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 6. Write a program to check that a given year is Leap Year or not.
year = int(input("Enter year : "))


if year % 100 == 0 and year % 400 == 0:
    print("Given century year is a Leap Year.")
elif not (year % 100 == 0) and year % 4 == 0:
    print("Given year is a Leap Year")
else:
    print("Given year is NOT a Leap Year")


# 7. Write a program in Python to find largest number among three numbers, Take input from user.

nums = list()

for x in range(3):
    nums.append(int(input(f"Enter num {x+1} : ")))

print(f"Largest number out of three provided is {max(nums)}")


# 8. Write a program to sum all the digits of an input number. [e.g. input number = 1234, sum = 1+2+3+4= 10]

sum = 0
num = input("Enter a number : ")

for x in num:
    sum += int(x)

print(f"The sum of all the digits of a given number is {sum}")
