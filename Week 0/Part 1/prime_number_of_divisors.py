def is_prime(n):
    if n < 0:
        n *= -1
    if n == 1:
        return False
    else:
        for numbers in range(2, n):
            if n % numbers == 0:
                return False
        return True


def prime_number_of_divisors(n):
    count = 0
    for number in range(1, n + 1):
        if n % number == 0:
            count += 1
    return is_prime(count)

print(prime_number_of_divisors(7))
print(prime_number_of_divisors(8))
print(prime_number_of_divisors(9))
