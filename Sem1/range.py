# Syntax -
# The range() function can take a maximum of three arguments: range(start, stop, step)
# If we pass a single argument to range(), it means we are passing the stop argument.
# If we pass two arguments to range(), it means we are passing start and stop arguments.
# The step argument specifies the incrementation/Difference between two numbers in the sequence.
# if only 0 or negative number is passed, we get an empty sequence.
# The default value of start is 0, and the default value of step is 1. That's why range(0, 5, 1) is equivalent to range(5).

# The range() function returns a sequence of numbers between the give range.
# range() returns an immutable sequence of numbers that can be easily converted to lists, tuples, sets etc.

#! TO PRINT THE NUMBERS WE CAN MAKE SETS , TUPLES , LISTS FROM IT OR WE CAN USE LOOPS.
randomNums = range(10)
print(randomNums)  # This will not print the numbers generated using range()

for x in randomNums:
    print(x, end=" ")

# OR

digits = list(randomNums)
factors = list(range(20))
factorsOfTwo = list(range(2, 21, 2))
print(digits, factors, factorsOfTwo)

x = tuple(range(-5, 6))
x = tuple(range(-5, 6, 2))
print(x)
