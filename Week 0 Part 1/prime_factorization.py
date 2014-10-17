def is_prime(n):
    if n < 0:
        n *= -1
    if n == 1:
        return False
    for numbers in range(2, n):
        if n % numbers == 0:
            return False
    return True


def repetition_in_list(list):
    new_list = []
    for item in list:
        fst = item
        snd = 0
        for num in range(0, len(list)):
            if fst == list[num]:
                snd += 1
        flag = True
        for items in range(0, len(new_list)):
            if (fst, snd) == new_list[items]:
                flag = False
        if flag:
            new_list.append((fst, snd))
    return new_list


def prime_factorization(n):
    list = []
    if n == 0:
        return 0
    if n == 1:
        return 1
    while n != 1:
        temp = n
        for x in range(2, n + 1):
            if n % x == 0:
                if is_prime(x):
                    n //= x
                    list.append((x))
            if n != temp:
                break
    return repetition_in_list(list)

print(prime_factorization(10))
print(prime_factorization(14))
print(prime_factorization(356))
print(prime_factorization(89))
print(prime_factorization(1000))
