# Reference - https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment/
# Unpacking is like destructuring in JS
# Unpacking in Python refers to an operation that consists of assigning an iterable of values to a tuple (or list) of variables in a single assignment statement.

# As a complement, the term packing can be used when we collect several values in a single variable using the iterable unpacking operator, *.

# Historically, Python developers have generically referred to this kind of operation as tuple unpacking.
# Nowadays, a more modern and accurate term would be iterable unpacking.
# As we can now use unpacking on almost any iterables.

#! Unpacking Tuples (Similar to Js destructuring)
# All three syntaxes are same for unpacking tuples.
a, b, c = 1, 2, 3
# a,b,c = (1,2,3)
# (a,b,c) = (1,2,3)
print(a)
print(b)
print(c)

# ~ This syntax of unpacking in wrong because at the LHS number of variables are not enough to unpack the given tuple.
# a, b = 1, 2, 3
# Traceback (most recent call last):
# ValueError: too many values to unpack (expected 2)

# ~ This syntax of unpacking in wrong because at the RHS number of items are not enough to assign to all variables.
# a, b, c = 1, 2
# Traceback (most recent call last):
# ValueError: not enough values to unpack (expected 3, got 2)

# ! Unapcking Strings
a, b, c, d = "8945"
print(a)
print(b)
print(c)
print(d)

# ! Unapcking Lists
name, age, course = ["Vaskar", 25, "MCA"]
print(name, age, course, sep="|")


# ~ Spread Operator in python for list

testList = ["Vaskar", 25, "MCA"]
print(*testList)

# ~ Spread Operator in python for dict
testDict = {"name1": "Vaskar", "University": "SVU", "Age": 25}
print({**testDict, "random": 234})
