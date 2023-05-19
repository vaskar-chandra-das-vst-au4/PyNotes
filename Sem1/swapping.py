a = 50
b = 12

# Method 1 - Using a temp variable
# temp = a
# a = b
# b = temp
# print(a)
# print(b)

# Method 2 - Using arithematic operators
# a = a + b  # 50 + 12 = 62
# b = a - b  # 62 - 12 = 50
# a = a - b  # 62 - 50 = 12
# print(a)
# print(b)


# Method 3 - Using bitwise operator XOR
# Reference - https://www.scaler.com/topics/xor-in-python/
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a)
# print(b)


# Method 4 - Using unpacking
# a, b = b, a
# print(a)
# print(b)
