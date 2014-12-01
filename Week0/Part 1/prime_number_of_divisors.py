from is_prime import is_prime


def prime_number_of_divisors(n):
    count = 0
    for number in range(1, n + 1):
        if n % number == 0:
            count += 1
    return is_prime(count)
