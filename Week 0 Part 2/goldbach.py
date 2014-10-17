def is_in_list(list, snd_list):
    for elem in list:
        if elem == snd_list[0]:
            return True
    return False


def is_prime(n):
    if n < 0:
        n *= -1
    if n == 1:
        return False
    for numbers in range(2, n):
        if n % numbers == 0:
            return False
    return True


def goldbach(n):
    result = []
    for num in range(2, n):
        temp_list = [(n- num, num)]
        if is_prime(num) and is_prime(n - num) and not is_in_list(result, temp_list):
            result.append((num, n - num))
    return result


print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))
