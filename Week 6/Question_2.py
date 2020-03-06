def findingGCD(m, n):
    while n >= 0:
        if n == 0:
            return m
        else:
            return findingGCD(n, m % n)
    else:
        print("Should be a valid positive number")


Implementation = findingGCD(15, 625)
print(Implementation)
