import keyword

print("Total number of keyword -", len(keyword.kwlist))
print(*keyword.kwlist, sep="\n")
