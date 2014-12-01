def sum_matrix(m):
    result = 0
    for lists in m:
        for number in lists:
            result += number
    return result
