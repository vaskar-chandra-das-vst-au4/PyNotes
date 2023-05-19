# #! SETS ->
# This is an unordered collection of elements.
# Every set element is unique(no duplicates)
# Elements are immutable i.e cant be changed
# They are aslo use to perform mathematical set operations like intersection .
# Indexes dont exist for sets.


# firstSet = {22, 34, 14, 56, 78}
# secondSet = {341, 45, 232, 89, 89, 89}
# print(firstSet, secondSet)

# ~ Construct sets from a list using set() function
# itemList = [23, 45, 45, 45, 45, "Paneer", "Pizza", "Avacado", 78.90]
# itemSet = set(itemList)
# print(type(itemSet), itemSet)

# ~ Creating an empty set
# We cant simply create empty set just writing a = {} because this will create an empty dict
# So for this we use set constructor function without passing any argument.
# a = set()  # Set
# x = {}  # Dict
# print(type(a), type(x))

# ~ Insertion in a Set using add() and update()
# Sets itself are mutable. However, since they are unordered, indexing has no meaning.
# We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.
# @ add() - Use to add a single element.
# itemSet.add(2000)
# print(itemSet)

# @ update() - can take tuples , lists ,strings and other sets as its argument. In all cases, duplicates are avoided.
# itemSet.update([9, 10, 11], {1, 4, 5}, "UPDATE_METHOD")
# print(itemSet)

# ~ Removing elements from a set
# A particular item can be removed from a set using the methods discard() and remove().
# They both take the element as a argument but both dont return anything. Just manupulate the original set.

# The only difference between the two is that the discard() function leaves a set unchanged if the element is not present in the set.
# On the other hand, the remove() function will raise an error in such a condition (if element is not present in the set).

# animalSet = {"dog", "cat", "cow", "tiger", "giraffe", 56.1, 86}

# (animalSet.remove(86))
# print(animalSet)
# animalSet.discard("tiger")
# print(animalSet)

# @ pop()  and clear() method for sets
# Since set is an unordered data type, there is no way of determining which item will be popped. It is completely arbitrary.
# can also remove all the items from a set using the clear() method.
# animalSet.pop()
# print(animalSet)

# animalSet.clear()
# OR
# del animalSet
# print(animalSet)

# ~ Python Set Operations
# Sets can be used to carry out mathematical set operations like union, intersection, difference and symmetric difference.

# @ Union Using Pipe operator |
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# print(a | b)
# OR
# print(a.union(b))

# @ Intersection
# print(a & b)
# print(a.intersection(b))

# @  intersection_update()
# finds the intersection of different sets and updates it to the set that calls the method.
# Syntax - A.intersection_update(*sets) # Here, *sets indicates that set A can be intersected with one or more sets.
# method doesn't return any value. Its update the set on which this method will be called
A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}

A.intersection_update(B, C)
print(A)
print("-------------")

# @ Difference
month1 = {"Jan", "Feb", "Mar", "Apr"}
month2 = {"Jan", "Feb", "May", "Jun"}
print(month1 - month2)
# OR
print(month1.difference(month2))

# @ Symmetric Difference
# It means (A U B) = A + B - (A ∩ B)
# In Output the common elements will not be present.
print(month1.symmetric_difference(month2))
# OR
print(month1 ^ month2)

# @ Comparisions
# Python allows us to use the comparison operators i.e., <, >, <=, >=, == with the sets by using which we can check whether a set is a subset, superset, or equivalent to other set. The boolean true or false is returned depending upon the items present inside the sets.
x = {1, 2, 3, 4, 5}
y = {1, 2}
z = {1, 2, 6}

# Is x is a superset of y?
print(x > y)
# Is x is a subset of y?
print(x < y)
# Do y and z are same?
print(y == z)


# ~ Membership Test
day = set(["tuesday", "wednesday"])
print("tuesday" in day)
print("monday" in day)
print("saturday" not in day)


# ~ FrozenSets
# Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.
# Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.
# They are immutable form of the normal sets, i.e., the items of the frozen set cannot be changed and therefore it can be used as a key in the dictionary.
# The elements of the frozen set cannot be changed after the creation. We cannot change or append the content of the frozen sets by using the methods like add () or remove ().
# The frozenset() method is used to create the frozenset object. The iterable sequence is passed into this method which is converted into the frozen set as a return type of the method.

immutableSet = frozenset([1, 2, 3, 4, 5])
print(type(immutableSet))
