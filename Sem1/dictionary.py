# Python dict are like JS Objects.
# dictionary is an ordered collection of items which present as a key - value pair.
# Dict are optimized to retrieve values when the key is known.


student1 = {
    "name": "Vaskar Chandra Das",
    "age": 25,
    "qualification": "MCA",
    "bloodGrp": "B+",
    "gender": "Male",
    "address": "Kalyani",
    "role": "developer",
}

# ~ Accessing values from dict
# values can be accessed using both box and dot notations.
# If we use the square brackets [], KeyError is raised in case a key is not found in the dictionary. On the other hand, the get() method returns None if the key is not found.
# we can provide a 2nd argument as a error message into get method which will be returned as a string.
print(f'Name of student 1 is {student1["name"]}.')
# OR
print(f"Name of student 1 is {student1.get('name')}.")

# student1["x"]
# student1.get("x")
print(student1.get("x", "Provided key not found!"))

# ~ Add or change dict items
student1["school"] = "Kendriya Vidyalaya No. 2 Kanchrapara"
student1["qualification"] = "Master of computer application"

# Adding multiple values for a single key
student1["places"] = "Shimla", "Europe", "Africa"

# ~ Remove items
# We can aslo use pop() and popitem() method to remove items.This method removes an item with the provided key and returns the value.
# student1.pop("role")
# print(student1)

# The popitem() method can be used to remove and return an arbitrary (key, value) item pair from the dictionary.
# student1.popitem()
# print(student1)

#  All the items can be removed at once, using the clear() method OR can also use the del keyword to remove individual items or the entire dictionary itself.
# student1.clear()
# del student1
print(student1)

# ~ Copy dict
# copy1 = student1.copy()
# print(copy1)

# ~ Iterating Dict
# By default x in for loop over dict is key.

# Print keys
for x in student1:
    print(x)
# OR
for x in student1.keys():
    print(x)

# Print values
for x in student1:
    print(student1[x])
# OR
for x in student1.values():
    print(x)

# Print items(key-value pair)
for x in student1.items():
    print(x)

for x, y in student1.items():
    # x - key and y - value
    print(f"The key is {x} and its value {y}.")

# ~ Print dict as a string using str() method
print(str(student1))

# ~ Get dict length
print(len(student1))
