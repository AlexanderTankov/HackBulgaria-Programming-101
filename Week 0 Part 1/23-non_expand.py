def nan_expand(times):
    result = " "
    if times == 0:
        return result
    else:
        result = "Not a NaN"
    for x in range(1, times):
        temp = result
        result = "Not a " + temp
    return result

print(nan_expand(0))
print(nan_expand(1))
print(nan_expand(2))
print(nan_expand(3))
