def sumSeries(number):
    sum = 0
    for i in range(1, number + 1):
        sum = sum + i
    return sum


print(sumSeries(2))
print(sumSeries(3))
