# rows = int(input("Enter the number of rows: "))

# for x in range(1, rows + 1):
#     print(str(x) * x)

# for x in range(1, rows + 1):
#     for y in range(x):
#         print(x, end="")
#     print()
# ! Reserved keyword
# import keyword

# print(keyword.kwlist)


# ! reverse string
# string = "abcd"
# print(string[::-8])
# # pep8 and repl

# ! Raise error
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# try:
#     if b == 12:
#         raise ValueError("Value error occur")
#     c = a / b
#     print("Result is : ")
#     print(c)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)

# ! Shorthand for if else loop
# a = 100
# b = 23
# # (true expression) if (condition) else (false expression)
# print("a is greater than b") if a > b else print("b is greater than a")
# import math
# from enumurateFn import welcome

# print(dir(math))

# print(math.floor(-3.546))  # rounds down
# print(math.ceil(-3.546))  # round up
# print(math.trunc(-3.546))  # cut decimal part

# welcome()


# ! Operator overloading
# class Vector:
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
#         # must return a string no print statement

#     def __add__(self, x):
#         return Vector(self.i + x.i, self.j + x.j, self.k + x.k)


# v1 = Vector(2, 3, 5)
# v2 = Vector(5, 7, 2)
# # print(v1 + v2)  # unsupported operand as add dunder method in this class is not defined
# # print(type(v1))  # <class '__main__.Vector'>

# print(v1 + v2)  # now it is working because add dunder method is defined
# print(type(v1 + v2))  # <class '__main__.Vector'>

list1 = [1, 21, 7]
list2 = [1, 21, 7]
print(list1 == list2)
