# Print Prime
prime = 2
limit = 1050
while prime != limit:
    for x in range(2, (prime // 2) + 1):
        if prime % x == 0:
            break
    else:
        print(prime)
    prime += 1
print(34 * 657)
