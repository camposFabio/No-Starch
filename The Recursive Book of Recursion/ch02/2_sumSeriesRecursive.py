def sumSeries(number):

    if (number < 1):
        return "Error"

    if (number == 1):
        # BASE CASE
        sum = number
    else:
        # RECURSIVE CASE
        sum = number + sumSeries(number - 1)

    return sum


print(sumSeries(2))
print(sumSeries(3))
print(sumSeries(4))
