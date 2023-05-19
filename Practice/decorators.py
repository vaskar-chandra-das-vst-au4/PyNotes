# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.
# ! decorators are similar to js first order functions -
# In Javascript, functions can be assigned to variables in the same way that strings or arrays can. They can be passed into other functions as parameters or returned from them as well. A “higher-order function” is a function that accepts functions as parameters and/or returns a function.


# ! one way of implementing additional functionality
# def new(a, b):
#     if a < b:
#         a, b = b, a
#     divide(a, b)


# new(2, 4)

# ! Now using design pattern- decorator


# def decorators(fn):
#     def inner(a, b):
#         if a < b:
#             a, b = b, a
#         return fn(a, b)

#     return inner


# def divide(a, b):
#     print(a / b)


# modifiedFn = decorators(divide)
# modifiedFn(2, 4)
# decorators(divide)(2, 4)


# OR - new syntax for decorators
# def testFn(fn):
#     def inner(*args, **kwargs):
#         return fn(*args, **kwargs)

#     return inner


# @testFn
# def greet(a, b):
#     print(f"The args are - {a} and {b}")


# greet(12, 34)


# ! find prime
# def findPrime():
#     num = int(input("Enter a number : "))
#     if num == 1:
#         return print("Not a Prime number")
#     for x in range(2, (num // 2) + 1):
#         if num % x == 0:
#             print("Not a Prime number")
#             break
#     else:
#         print(f"{num} is a prime number")


# findPrime()
