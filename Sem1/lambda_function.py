from functools import reduce

primeNumbers = [2, 3, 5, 7, 11, 13, 17]

# double = lambda a: print(a * 2)
# for p in primeNumbers:
#     double(p)

# ~ Filter
singleDigit = list(filter(lambda x: x < 10, primeNumbers))
print(singleDigit)

# ~ Map
triple = list(map(lambda x: x * 3, singleDigit))
print(triple)

# ~ Reduce

sum1 = reduce(lambda a, b: a + b, triple)
print(sum1)
