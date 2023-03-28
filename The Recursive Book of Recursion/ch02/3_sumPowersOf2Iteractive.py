def sumPowersOf2(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + 2**i

    return sum


print(sumPowersOf2(1))
print(sumPowersOf2(2))
print(sumPowersOf2(3))
