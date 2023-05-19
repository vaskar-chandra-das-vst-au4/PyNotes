# Reverse
primeNum = [2, 3, 5, 7, 11, 13, 17]


def reverse(arr):
    for x in range(len(arr) // 2):
        arr[x], arr[-(x + 1)] = arr[-(x + 1)], arr[x]

    return print(arr)


reverse(primeNum)
