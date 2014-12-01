def nth_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return nth_fibonacci(n-1) + nth_fibonacci(n-2)


def nth_fibonacci_second(n):
    a = 0
    result = 1
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    for digit in range(1, n):
        b = result
        result = a + b
        a = b
    return result
