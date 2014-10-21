def nan_expand(times):
    result = ""
    if times == 0:
        return result
    else:
        result = "Not a NaN"
    for x in range(1, times):
        temp = result
        result = "Not a " + temp
    return result
