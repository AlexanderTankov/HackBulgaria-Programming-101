def is_decreasing(seq):
    for x in range(0, len(seq) - 1):
        if seq[x] <= seq[x + 1]:
            return False
    return True

print(is_decreasing([5, 4, 3, 2, 1]))
print(is_decreasing([1, 2, 3]))
print(is_decreasing([100, 50, 20]))
print(is_decreasing([1, 1, 1, 1]))
