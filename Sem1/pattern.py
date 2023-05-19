# # Pattern 1:
# # # # #
# # # # #
# # # # #
# # # # #
# print("Pattern 1")
# for r in range(4):  # This for loop makes rows
#     for c in range(4):  # This for loop makes columns
#         print("#", end=" ")
#     print()

# # Pattern 2:
# #
# # #
# # # #
# # # # #
# print("Pattern 2")
# for r in range(4):  # This for loop makes rows
#     for c in range(r + 1):  # This for loop makes columns
#         print("#", end=" ")
#     print()

# # Pattern 3:
# # # # #
# # # #
# # #
# #
# print("Pattern 3")
# for r in range(4):  # This for loop makes rows
#     for c in range(4 - r):  # This for loop makes columns
#         print("#", end=" ")
#     print()


# OR
for i in range(4):
    print("# " * (4))
for i in range(4):
    print("# " * (4 - i))
for i in range(4):
    print("# " * (i + 1))
