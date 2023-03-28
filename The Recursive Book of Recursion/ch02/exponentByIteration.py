def exponnentByIteration(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result


print(exponnentByIteration(3, 6))
print(exponnentByIteration(10, 3))
print(exponnentByIteration(17, 10))
