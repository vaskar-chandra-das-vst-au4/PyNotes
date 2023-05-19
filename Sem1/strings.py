# #! Strings ->
# # String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings. Multi-line strings can be denoted using triple quotes, ''' or """.
# # String Index - Is similar as present in javaScript
# # Strings are immutable.

# # Reverse indexing starts with -1 but not with 0.
# name = "Vaskar Chandra Das"
# print(name[2])
# print(name[-1])  # Last Character
# print(name[-2])  # 2nd Last Character
# print(name[0:3])  # Print character 0 , 1 and 2 . 3 will not be included
# print(
#     name[2:]
# )  # Unspecified end will ṣlead to print all characters from index 2 to last
# print(name[:-2])  # From 1st to 2nd last character
# print(
#     name[3:23]
# )  # Print from 3rd to the last character despite of not having index 23 in the string.
# # @ Find length of a string using "len" function
# print(f"My name contains {len(name)} characters.")

# # @ Convert any Iterable into String using Join method
# # Syntax - "string".join("Iterable")
# myTuple = ("John", "Peter", "Vicky")

# x = "--".join(myTuple)

# print(x)


# @ Capitilize method
# This method manupluate the original string and aslo return the same.
name = "vaskar chandra das"
print(name.capitalize())

# @ Center method
print(name.center(50, "+"))

# @ Count method - same as others
