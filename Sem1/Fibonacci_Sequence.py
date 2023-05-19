# Write a function which output a Fibonacci series where number of terms are taken from an user.
# Enter number of terms you needed in the series: 10
# 0 1 1 2 3 5 8 13 21 34
def fibonacciSeriesMaker1(limit):
    series = [0, 1]

    if limit < 0:
        print("Negative integer is not allowed! Please enter a positive integer.")
    if limit == 0 or limit == 1:
        print(0)
    if limit == 2:
        print(*series)
    if limit > 2:
        for x in range(limit - 2):
            series.append(series[-1] + series[-2])
        print(*series)


userLimit1 = int(input("Enter number of terms you needed in the series: "))
fibonacciSeriesMaker1(userLimit1)


# Write a function which output a Fibonacci series upto a number provided by an user.
# Enter a number upto which you want the series: 10
# 0 1 1 2 3 5 8
def fibonacciSeriesMaker(limit):
    series = [0, 1]

    if limit < 0:
        print("Negative integer is not allowed! Please enter a positive integer.")
    if limit == 0 or limit == 1:
        print(0)
    if limit == 2:
        print(*series)
    if limit > 2:
        while max(series) < limit:
            series.append(series[-1] + series[-2])
        series.remove(max(series))
        print(*series)


userLimit = int(input("Enter a number upto which you want the series: "))
fibonacciSeriesMaker(userLimit)
