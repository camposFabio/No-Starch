def fibonacci(nthNumber):
    a, b = 1, 1
    print('a = %s, b = %s' % (a, b))
    for i in range(1, nthNumber):
        a, b = b, a + b  # Get the next Fibonacci number.
        print('a = %s, b = %s' % (a, b))
    return a


print(fibonacci(10))


def fibonacci(nthNumber):
    a, b = 1, 1
    print('a = %s, b = %s' % (a, b))
    for i in range(1, nthNumber - 1):
        a, b = b, a + b  # Get the next Fibonacci number.
        print('a = %s, b = %s' % (a, b))
    return b


print(fibonacci(10))
