def nth_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return nth_fibonacci(n-1) + nth_fibonacci(n-2)


def nth_fibonacci_second(n):
    a = 0
    sum = 1
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    for digit in range(1, n):
        b = sum
        sum = a + b
        a = b
    return sum

print(nth_fibonacci(1))
print(nth_fibonacci(2))
print(nth_fibonacci(3))
print(nth_fibonacci(10))

print(nth_fibonacci_second(1))
print(nth_fibonacci_second(2))
print(nth_fibonacci_second(3))
print(nth_fibonacci_second(10))
