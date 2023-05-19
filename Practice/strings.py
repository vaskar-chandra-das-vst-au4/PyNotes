sample = "Vaskar Chandra Das"

#! Captitilize , lower , upper ,swapcase, title , isTitle , isUpper and isLower
print(sample.capitalize())
print(sample.lower())
print(sample.swapcase())
print(sample.upper())
print(sample.title())
print(sample.istitle())
print(sample.isupper())
print(sample.islower())

# ! center ljust and rjust
print(sample.center(50, "-"))
print(sample.ljust(50, "+"))
print(sample.rjust(50, "+"))

# ! Count chr
# .count(find , start , end)
print(sample.count("a"))
print(sample.count("a", 0, 2))

# ! endswith and startswith
# value can be chr string or any tuple with possible values
# .startsWith(value, start , end)
# .endsWith(value, start , end)
print(sample.startswith("V"))  # case sensitive
print(sample.endswith("V"))
print(sample.endswith(("V", "v", "r", "s")))


#! find rfind and index
# .find(value , start , end) - if found return first index otherwise -1
# rfind(value , start , end) - if found return highest index otherwise - 1
# index(value , start , end) - if not found then throw error otherwise return index

# ! strip lstrip and rstrip
# returns a copy of the string by removing both the leading and the trailing characters (based on the string argument passed)
sample = "    hello"
print(
    sample.strip(" ")
)  # print(sample.strip()) = print(sample.strip(" ")) != print(sample.strip(""))

# ! split and join
# The string join() method returns a string by joining all the elements of an iterable (List, Tuple, String, Dictionary and Set.), separated by the given separator.The syntax of the join() method is: string.join(iterable)
# For dict - If the key of the string is not a string, it raises the TypeError exception.
# aslo data type's element must be a string to concatentate.

# The split() method splits a string at the specified separator and returns a list of substrings.The syntax of split() is: str.split(separator, maxsplit)
# method takes a maximum of 2 parameters: separator (optional)- Delimiter at which splits occur. If not provided, the string is splitted at whitespaces AND maxsplit (optional) - Maximum number of splits. If not provided, there is no limit on the number of splits.

num = [1, 4, 6, 7]
for x in num:
    print(x, end="")
# or
num = ["2", "b", "7"]
print("".join(num))

cars = "BMW-Telsa-Range Rover"
print(cars.split("-"))

# ! Replace
# .replace(old ,new , times) - default times = all
# The replace() method can take a maximum of three arguments:
# old - the old substring we want to replace
# new - new substring which will replace the old substring
# count (optional) - the number of times you want to replace the old substring with the new string
# Note: If count is not specified, the replace() method replaces all occurrences of the old substring with the new string.

sample = "Dog is a very good companion."
print(sample.replace("a very good", "an excellent"))

# ! isalnum , isalpha , isdigit , isdecimal , isnumeric , isspace , isprintable
# isalnum - true for A-Z , a-z and 0-9
# isalpha - true for A-Z and a-z
