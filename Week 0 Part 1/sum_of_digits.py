def sum_of_digits(n):
    sum = 0
    while n != 0:
        if n < 0:
            n *= -1
        sum += n % 10
        n //= 10
    return sum

print(sum_of_digits(1325132435356))
print(sum_of_digits(123))
print(sum_of_digits(6))
print(sum_of_digits(-10))
