# age = int(input("Enter your age :"))
# if age >= 20 and age <= 25:
#     print("Entered age is allowed for swimming in the campus")
# else:
#     print("Entered age is not allowed for swimming in the campus")

# mylist = [12, 56, "vaskar", 89, 77]
# print(type(len(mylist)))

# rows = int(input("Enter number of rows"))
# for i in range(0, rows + 1):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# table = int(input("Number : "))

# for x in range(1, 11):
#     print(f"{table} X {x} = {table * x}")

# v = 2
# while v != 3:
#     print("a")
# print(1 % 2)\

# number = int(input("Enter a positive number: "))
# binary = 0
# place = 1
# n = number
# while n > 0:
#     remainder = int(n % 2)
#     binary = binary + remainder * place
#     place = place * 10
#     n = n / 2
# print("Binary representaion of", number, "is", binary)


# inputList = [1, 2, 3, 4, 5, 6, 7]
# # outputList = [5,6,7,1,2,3,4]

# step = int(input("Enter step:"))
# if step > 0:
#     outputList = [*inputList[-step:], *inputList[:-step]]
#     print(outputList)
# else:
#     print("Enter a non-negative Integer!")


# list1 = [1, 2, 3]
# print(type(*list1)) we cant do this
# print(*list1)
# a, b, c = list1
# print(a)
# print(b)
# print(c)

# index = 1
# for x in range(1, 10, 2):
#     print(str(x) * index)
#     index += 1
# print(type(id(index)))
# print(id(index))
# ! Key can be tuple , string , number and frozenset
# # myDict1 = {(1, 2): "I am a TUPLE", {45, 78}: "I am a SET"}
# myDict = {(1, 2): "I am a TUPLE", frozenset([45, 78]): "I am a FROZENSET"}
# print(myDict)
#! find the largest of three number
# try:
#     a = int(input("Enter an integer:"))
#     b = int(input("Enter an integer:"))
#     c = int(input("Enter an integer:"))
#     if a > b and a > c:
#         print(f"{a} is the greatest among all three.")
#     elif b > c:
#         print(f"{b} is greatest of all")
#     else:
#         print(f"{c} is greatest of all")
# except ValueError as e:
#     print(e)

# enteredNumbers = [a, b, c]
# print(f"{max(enteredNumbers)} is the greatest number among all three.")

#! find Even number between 1 to 50
# for x in range(2, 51, 2):
#     print(x, end=" ")

# ! Check the number is prime or not
# prime = True
# a = int(input("Enter a number :"))

# if a > 1:
#     for x in range(2, a):
#         if a % x == 0:
#             print(f"{a} is not a prime number.")
#             prime = False
#             break

#     if prime:
#         print(f"{a} is a prime number.")
# else:
#     print(f"{a} is neither prime nor composite.")


#! Dict to list
# myDict = {
#     "a": "apple",
#     "b": "ball",
#     "c": "cat",
#     "d": "dog",
# }

# print(list(myDict))  # only keys are included in list

# myList = []
# for x, y in myDict.items():
#     myList.append(x)
#     myList.append(y)
# print(myList)  # both keys and values are included in list

# ! list to dict
# list1 = [("a", 1), ("b", 2), ("c", 3)]

# print(dict(list1))
# OR
# myDict = {}
# for x, y in list1:
#     myDict[x] = y

# print(myDict)


# ! == vs is
# Based on my observation if two variables are assigned with tuples ,strings or integers then they  will be allocated same memory address so in this case is operator would return True if we compare them.because tuples , strings and integers are completely immutable.
# When we assign two variables with same string or integer or tuple(sequence of elements should be same) or list(sequence of elements should be same) and we compare them using equality operator , it will return True.but it shows slight different behaviour for dict and sets, if both var have same items even in different order , it will return true for them , this is due to the fact that both sets and dict are non indexed so equality operator only checks for the items not for their order.
