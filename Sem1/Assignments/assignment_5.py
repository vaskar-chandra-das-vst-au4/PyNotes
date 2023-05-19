# 1. Write a Python program to create a tuple with different data types.
mixedData = (1, "Vaskar", 12.4, True)

# 2. Write a Python program to unpack a tuple in several variables and print the sum of those variables.
a, b, *c = mixedData
p, q, r, s = mixedData
print(a, b, c)
print(p, q, r, s)

# 3. Write a Python program to convert a tuple to a string
tuple1 = (1, 2, True, "Vaskar", 23, 67)
string1 = ""
for x in tuple1:
    string1 += f" {str(x)}"

print("I am a string", string1)

# 4. Write a Python program to get the 4th element and 4th element from last of a tuple
def elementExtractor(givenTuple):
    print(givenTuple[4])
    print(givenTuple[-4])


elementExtractor(tuple)

# 5. Write a Python program to convert a list to a tuple.
givenList = [1, 2, 4]
convertedTuple = tuple(givenList)

# 6. Write a Python program to reverse a tuple and find length of the tuple.
print(tuple(sorted(convertedTuple, reverse=True)))
# OR
sortedTuple = convertedTuple[::-1]
print(sortedTuple)

print(len(convertedTuple))

# 7. Write a Python program to convert a tuple to a dictionary.
# input tuple_1
inputTuple_1 = ("TutorialsPoint", "Python", "Codes")

# input tuple_2
inputTuple_2 = (5, 6, 7)

# printing the input tuple_1(keys)
print("The input Tuple_1(keys) = ", inputTuple_1)

# printing the input tuple_2(values)
print("The input Tuple_2(values) = ", inputTuple_2)

# Checking whether the length of both the tuples are equal or not
if len(inputTuple_1) == len(inputTuple_2):

    # converting both the tuples into a dictionary using zip()
    # and dict() functions
    # Here zip function takes elements of input tuple 1 as keys and input tuple 2 elements as values
    # Then we convert this to a dictionary using dict()
    resultDictionary = dict(zip(inputTuple_1, inputTuple_2))
    # printing result dictionary from the given two tuples
    print("The result dictionary:", resultDictionary)

# OR
givenTuple2 = (("A", "Apple"), ("B", "Boy"), ("C", "Cat"))
newDict = dict((a, b) for a, b in givenTuple2)
print(newDict)
# OR
newDict3 = dict()
for x, y in givenTuple2:
    newDict3[x] = y

print("created using for loop-", newDict3)

# 8. Write a Python program to convert a list of tuples into a dictionary.
givenList2 = [("A", "Apple"), ("B", "Boy"), ("C", "Cat")]
newDict1 = dict((a, b) for a, b in givenList2)
print(newDict1)

# OR
newDict4 = dict()
for x, y in givenList2:
    newDict4[x] = y

print(newDict4)
