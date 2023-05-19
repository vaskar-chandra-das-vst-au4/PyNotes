# # ! TUPLE ->
# # Tuple are immutable lists.
# # Tuple is used to store the sequence of immutable Python objects.
# # Tuple and list are similar but unlike list Tuples are immutables. That is their elements cant be changed once assigned during creation.
# # We use round brackets i.e parenthesis to create tuple.
# # tuple can have duplicate elements.
# # A tuple can have any number of items and they may contain different types (integer, float, list, string, etc.).
# # Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically.

# digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(digits[2])
# # digits[2] = 45 # TypeError: 'tuple' object does not support item assignment

# randomValues = ("Neo", 567, 9.67, "Dog")  # Contain different data types.

# nestedTuple = ((1, 2, 3), "cat", 89, randomValues, 89, 54, 89, 12, 4, 89)

# print(nestedTuple)

# # ~ A tuple can also be created without using parentheses. This is known as tuple packing
# squareNumbers = 1, 4, 9, 16, 25
# print(squareNumbers)

# # ~ Create a tuple with single element
# #@ Directly passing a single element in a tuple will not create a tuple. So to build a tuple using a single element we need to put a comma after that element.
# singleton = 1
# print(type(singleton))  # type - int

# singleton1 = (1,)
# print(type(singleton1))  # type - tuple

# # ! Accessing elements using index works for tuple as tuple is aslo a sequential data type.
# # ! Slice operator aslo used to fetch element.

# # ~ Mutable Objects within tuple can be reassigned
# subjects = ("Science", "Math", ["Physics", "Chemistry"])

# subjects[2][1] = "Biology"
# print(subjects)

# # ~ We can use + operator to combine two tuples. This is called concatenation

# print((1, 2, 3) + (4, 5, 6))
# print(("PYTHON",) * 5)

# # ~ Deleting a Tuple
# #! Deleting entire tuple is possible but elements of it cant be deleted.
# # del subjects
# # print(subjects)

# # ~ Methods count and index are available
# # But methods which are used to mutate elements are not available.

# # ~ Other methods
# # @ Check for a element in a tuple using is keyword
# # @ Returns Boolean
# odd = (1, 3, 5)
# print(5 in odd)
# print(10 in odd)

# # ~ Iterating on a tuple using for loop
# for num in odd:
#     print(num * 100)

# # @ Sum
# numbers = (20, 40, 50, 100, 60, 19, 500, 345)
# sum = 0
# for n in numbers:
#     sum += n

# print("Numbers are", numbers)
# print(f"Sum of all numbers present in tuple numbers is {sum}.")

# # ~ Print all elements of a tuple with its index
# i = 0
# for n in numbers:
#     print(f"Index {i} : {n}")
#     i += 1
