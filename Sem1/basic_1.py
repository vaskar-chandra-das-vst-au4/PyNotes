#
# #! BASICS

# import math
# from math import pi

# print("Python Tutorial")
# print(type("Hello World!"))

# # ! Important Data Types
# # Numbers/Numeric(Int,float,complex - Clases)
# # bool - Boolean - True(1)/False(0)
# # Sequencial - str , list, range and tuple
# # set
# # dict

# # @ Besides these We can create our own data types called Classes.

# # @ Other than these we aslo have specialized data type in the form of packages or modules which we import according to our need.

# #! Numbers and Float ->
# # @ Float take more memory than int.
# # @ We can do all basic arithematic calculation using numbers and float like in javaScript.
# print(type(2 - 4))
# print(2**4)  # 2 to the power 4
# print(5 // 4)  # Round down to integer
# print(5 % 4)  # Modular Operator = remainder

# #! Math Functions ->
# # Rounding ->
# x = round(3.4)
# print(x)
# # abs return absolute value
# print(abs(-56))


# # @  Binary representation - USING bin()
# # @ 0b101 - 0b is the indicator and 101 is the actual representation.
# print(bin(5))
# # ~  Returning a int from binary -
# print(int("0b101", 2))
# avg_Number = 23
# print("hello", x, avg_Number)


# #! Multiple Assignments ->
# age, name, course = 25, "Vaskar Chandra Das", "MCA"
# print(name, age, course)

# age1 = age2 = age3 = 78
# print(age1, age2, age3)

# #! Modules ->
# print(math.pi)
# print(math.sqrt(64))
# print(type(math))

# #! Output ->
# # @ By default print function has end='\n' which means each print function will added to new line.
# # @ Here by default end is a space that why we are getting between both the arguments provided to print function.
# # @ using end we can specify the gap between print functions.
# print("My name is", name, end="----and----")
# school_name = "Kendriya Vidyalaya No 2 Kanchrapara"
# print("My school name is", school_name)

# #! Output formatting ->
# # @ this is like template string of javaScript.
# # @ in format function sequence of variables are maintained. So the container present in the string will be filled according to the index of variables passed into format function.
# # @ we can aslo specify the index of varibles manually.
# print(
#     "My name is {} of {} yrs old. I have completed my schooling from {}.".format(
#         name, age, school_name
#     )
# )
# # @ Note : F-strings are faster than the two most commonly used string formatting mechanisms, which are % formatting and str.format().
# print(
#     f"My name is {name} of {age} yrs old. I have completed my schooling from {school_name}."
# )


# print("I love {0} and {1}.".format("bread", "butter"))
# print("I love {1} and {0}.".format("bread", "butter"))

print("Hello {name}, {greeting}!".format(name="Vaskar", greeting="Good Morning"))
print("Hello {greeting}, {name}!".format(name="Vaskar", greeting="Good Morning"))

# #! Operator precedence ->
# # @ Operator precedence -> same as in javaScript.
# # @ () , ** , *  /, +  -
# print((20 - 3) + 2**2)

# # ! Escape sequence
# print("Vaskar's car")
# print('Mamata\'s "House"')

# # @ Print Vaskar 10 times without actually writing -
# print("Vaskar" * 10, sep="")

# # @ Printing raw string.. "r" tells the python to ignore the \n or \v
# print(r"c:\docs\vaskar")

# # ! Comments
# # Python does not really have a syntax for multi line comments.
# # To add a multiline comment you could insert a # for each line:
# # Or, not quite as intended, you can use a multiline string.
# # Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

#! WE CAN DECLARE A EMPTY VARIABLE USING "NONE"

#! HELP
# we can read documentations on terminal using help() function

#! Garbage collection
# Unreferenced objects which are not linked to any indentifier are later be garbage collected.
