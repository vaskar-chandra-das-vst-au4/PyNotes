#
#! Linear Search
num = [23, 45, 12, 1]
find = 1


def findIndex(arr, toFind):
    for x in range(len(arr)):
        if arr[x] == toFind:
            return print(x)
    return print(-1)


findIndex(num, find)


#! Binary Search
num = [3, 4, 5, 9, 12]
find = 13

# @ Recursive method
def findIndexRec(arr, toFind, high, low):
    mid = (high + low) // 2

    if low > high:
        return print(-1)
    elif toFind == arr[mid]:
        return print(mid)
    elif toFind > arr[mid]:
        return findIndexRec(arr, toFind, high, mid + 1)
    else:
        return findIndexRec(arr, toFind, mid - 1, low)


findIndexRec(num, find, len(num) - 1, 0)

# @ Iterative method
def findIndexIter(arr, toFind, high, low):
    while high >= low:
        mid = (high + low) // 2
        if toFind == arr[mid]:
            return print("Index =", mid)
        elif toFind > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    print("Item not found.")


findIndexIter(num, find, len(num) - 1, 0)
