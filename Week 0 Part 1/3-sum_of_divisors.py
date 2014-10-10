def sum_of_divisors(n):
    sum = 0
    for number in range(1, n + 1):
        if n % number == 0:
            sum += number
    return sum

print(sum_of_divisors(8))
print(sum_of_divisors(7))
print(sum_of_divisors(1))
print(sum_of_divisors(1000))
