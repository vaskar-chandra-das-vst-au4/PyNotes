# Sort List - Bubble sort
def sortList(num):
    loop = len(num) - 1

    for y in range(loop):
        for x in range(loop):
            if num[x] > num[x + 1]:
                num[x], num[x + 1] = num[x + 1], num[x]
            else:
                continue

    print(num)


collection = [23, 45, 12, 1, 90, 34, 23, 67, 100, 25, 6, 5]
sortList(collection)
