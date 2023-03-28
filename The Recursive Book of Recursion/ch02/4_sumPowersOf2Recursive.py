def sumPowersOf2(n):
    sum = 0

    if (n == 1):
        # BASE CASE
        sum = 2
    else:
        # RECURSIVE CASE
        sum = 2**n + sumPowersOf2(n - 1)

    return sum


print(sumPowersOf2(1))
print(sumPowersOf2(2))
print(sumPowersOf2(3))
