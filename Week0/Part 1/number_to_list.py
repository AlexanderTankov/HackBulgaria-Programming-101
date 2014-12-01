def number_to_list(n):
    result = []
    while n != 0:
        result.append(n % 10)
        n //= 10
    result.reverse()
    return result
