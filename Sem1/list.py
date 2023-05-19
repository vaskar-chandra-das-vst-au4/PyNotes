# #
# #! LIST ->
# # @ Reference : https://www.programiz.com/python-programming/list
# # @ List in python is like array in javaScript.
# # @ We can store multiple objects of different data types in a single list.
# # @ Lists are mutable, meaning their elements can be changed unlike string or tuple.
# # @ We can access a range of items in a list by using the slicing operator ":".


# primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19]
# compositeNumbers = [4, 6, 8, 9, 10, 12, 14, 15, 16]
# mixedData = ["Vaskar", 45, 9.8, "d", "Denmark"]
# nestedList = [primeNumbers, compositeNumbers, 23, 67, "NestedList"]

# print(primeNumbers)  # Print whole list
# print(primeNumbers[3])  # Print element of index 3
# print(primeNumbers[-1])  # Last element
# print("List of odd prime numbers between 0 to 20 -", primeNumbers[1:])
# print(primeNumbers[1:-5])
# print(nestedList[0][1])  # Nested indexing
# print(nestedList)

# # @ Mutating elements -
# nestedList[0] = "Prime Numbers"
# nestedList[1:4] = [1, 2, 3]
# print(nestedList)


# # @ List functions/Mehtods -
# # ~ Append and Extend
# mixedData.append(1000)  # Add elements to the end
# mixedData.extend([10, 20, 30, 40, 50])  # Add a whole list to the end
# print(mixedData)
# # ~ Concatenating and Repeating
# print(primeNumbers + compositeNumbers + ["Prime + Composite"])
# constantNum = [24] * 10
# print(constantNum)

# # ~ Insert method
# # First parameter is Index Number to which we want to insert an element and 2nd one is for the element itself.
# rollNumber = [2, 3, 4, 5]
# print("Roll Numbers", rollNumber)
# rollNumber.insert(0, 1)
# print(rollNumber)
# rollNumber[4:3] = [100, 100, 100]
# print(rollNumber)
# rollNumber[8:3] = [6, 7, 1 + 7]
# print(rollNumber)

# # ~ Delete Elements
# # @ Using del
# weekDays = ["sun", "mon", "tue", "wed", "thru", "fri", "sat"]
# weekDaysCopy = ["sun", "mon", "tue", "wed", "thru", "fri", "sat"]
# del weekDaysCopy[2]
# print(weekDaysCopy)
# del weekDaysCopy[1:4]
# print(weekDaysCopy)
# del weekDaysCopy
# # print(weekDaysCopy) # Not defined
# # @ Using Remove - Need to provide the exact element as parameter
# weekDays.remove("sun")
# print(weekDays)
# # @ Using pop function which takes index
# weekDays.pop()  # Removes last element if index is not given
# print(weekDays)
# weekDays.pop(-2)
# print(weekDays)
# # @ Empty whole list using clear function
# weekDays.clear()
# print(weekDays)
# # @ We can aslo del elements by assigning a empty list
# wages = [200, 300, 130, 500, 789, 1000, 346]
# wages[0:3] = []
# print(wages)

# # ~ Make a copy of existing List
# wagesCopy = wages.copy()
# print(wagesCopy)

# # ~ Min And Max
# print(min(wages), max(wages))

# # ~ Total length
# print(len(wages))

# # ~ Count occurence of any element using Count method
# # This method only takes one argument which is an element. This method returns the number of times element appears in the list.
# # Syntax - list.count(element)
# wages.extend([100, 100, 100, 100, 100])
# print(wages.count(100))

# # ~ Sort using Sort method
# # By default, sort() doesn't require any extra parameters. However, it has two optional parameters:
# # reverse - If True, the sorted list is reversed (or sorted in Descending order)
# # key - function that serves as a key for the sort comparison
# # The sort() method doesn't return any value. Rather, it changes the original list.
# # Syntax - list.sort(key=..., reverse=...) order of argument doesnt matter.

# # Alternatively, you can also use Python's built-in sorted() function for the same purpose.
# # Syntax - sorted(list, key=..., reverse=...)

# # Note: The simplest difference between sort() and sorted() is: sort() changes the list directly and doesn't return any value, while sorted() doesn't change the list and returns the sorted list.

# # @ Ascending Order
# num = [10, 67, 89, 12, 9, 500, 89]
# num.sort()
# wages.sort()

# # sort method does not return a list. So below codes will return NONE only.
# # print(num.sort())
# # print(wages.sort())

# print(num)
# print(wages)

# # @ Descending Order
# primeNum1 = [2, 3, 5, 7, 11, 13, 17, 19]

# # Original list is not mutated
# print(sorted(primeNum1, reverse=True))
# print(primeNum1)

# # Original list is mutated
# primeNum1.sort(reverse=True)
# print(primeNum1)

# # ~ Find Index of a element
# # Syntax - list.index(element, start, end)
# # element - the element to be searched
# # start (optional) - start searching from this index
# # end (optional) - search the element up to this index
# # Returns the index of the given element in the list.
# # If the element is not found, a ValueError exception is raised.
# # Note: The index() method only returns the first occurrence of the matching element.
# friends = ["Vaskar", "Mamata", "Basanti", "Keshab", "Vaskar", "Mamata"]
# print(friends.index("Mamata"))
# print(friends.index("Vaskar", 1, -1))
# print(friends.index("Vaskar", 1, 3))


# # ~ Reverse List Elements
# # Syntax - list.reverse()
# # This method doesn't take any arguments.
# # Doesn't return any value. It updates the existing list.
# friends.reverse()
# print(friends)

# ! Dynamic list creation
nums = [x * 12 for x in range(100)]
print(nums)

nums = [x / 2 for x in range(100) if x % 2 == 0]
print(nums)

# ! Membership checking
if 10 in nums:
    print("Yes")
else:
    print("No")

if "V" in "hasdhsaV":
    print("Yes")
else:
    print("No")
