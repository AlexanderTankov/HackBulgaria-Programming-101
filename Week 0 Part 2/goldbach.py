from is_prime import is_prime


def is_in_list(list, snd_list):
    for elem in list:
        if elem == snd_list[0]:
            return True
    return False


def goldbach(n):
    result = []
    for num in range(2, n):
        temp_list = [(n - num, num)]
        if is_prime(num) and is_prime(n - num) and not is_in_list(result, temp_list):
            result.append((num, n - num))
    return result
