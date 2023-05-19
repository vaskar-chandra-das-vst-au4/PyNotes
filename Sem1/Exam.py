# # 1 - Write a python function that takes a list and returns a new list with unique elements of the first list.
sampleList = [1, 2, 3, 3, 3, 3, 4, 5]


def uniqueListMaker(inputlist):
    uniqueList = list(set(inputlist))
    return print(f"This is your list of unique elements {uniqueList}")


uniqueListMaker(sampleList)

# # OR
uniqueList = list()


def uniqueListMakeOR(inputList):
    for x in inputList:
        if x not in uniqueList:
            uniqueList.append(x)

    return print(f"This is your list excluding all duplicate elements {uniqueList}")


uniqueListMakeOR(sampleList)

# # 2 . Write a python program to count the even and odd numbers in a given list of integers using lambda function.


# givenList = [1, 2, 3, 5, 7, 8, 9, 10]
def countEvenAndOdd(givenList):
    evens = len(list(filter(lambda x: x % 2 == 0, givenList)))
    odds = len(list(filter(lambda x: x % 2 != 0, givenList)))
    return print(
        f"Number of even numbers in the given list is {evens} \nNumber of odd numbers in the given list is {odds}"
    )


countEvenAndOdd([1, 2, 3, 5, 7, 8, 9, 10])


# 3. Write a python program to create a lambda function that adds 15 to a given number passed in as an argument aslo create a lambda function that multiplies argument x with argument y and print the result.

adder = lambda x: print(x + 15)
adder(45)


sum = lambda x, y: print(x + y)
sum(13, 34)
