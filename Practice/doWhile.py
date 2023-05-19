n = 2

while 1:
    for x in range(2, (n // 2) + 1):
        if n % x == 0:
            break
    else:
        print(n)
    n += 1
    if n == 1000:
        break

# OR
n = 0
while True:
    print(n)
    n += 1
    if n == 50:
        break
