def groupby(func, seq):
    result = {}
    for num in seq:
        key = func(num)
        if key in result:
            result[key].append(num)
        else:
            result[key] = [num]
    return result
