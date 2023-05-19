import math
import random
import time
import os

# ! Math
print(math.ceil(12.3))  # round up
print(math.floor(12.3))  # round down
print(math.pi)  # pi value
print(math.sqrt(8))  # return square root
print(math.trunc(12.3345))  # cut decimal part

# ! Random
print(random.randint(0, 7))  # random number from 0 to 7 , 7 is included
mylist = [1, 2, 4]
random.shuffle(mylist)  # suffle iterable elements
print(mylist)

# ! Time
print(time.time())  # time from 1 jan 1970 midnight
print(time.ctime())  # show current time

print("Hello")
# time.sleep(3)  # delay for 3 seconds , arg - seconds
print("world")

# ! OS

# @  get current working directory and change directory
print("Path :", os.getcwd())
# os.chdir("../")
# print("Path :", os.getcwd())

# # @  Make directory
# # os.mkdir("./data")
# if not os.path.exists("./data"):
#     for x in range(1, 51):
#         os.mkdir(f"./data/Day {x}")

# # @  List directory
# print(*os.listdir("./data"), sep="\n")

# # @ Rename file
# os.rename("./data", "./dataRenamed")

# # @  delete a file
# if os.path.exists("./dataRenamed"):
#     os.remove("./dataRenamed")

# ! List modules
print(help("modules"))
