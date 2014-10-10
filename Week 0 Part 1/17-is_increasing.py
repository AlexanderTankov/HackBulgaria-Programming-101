def is_increasing(seq):
    for x in range(0, len(seq) - 1):
        if seq[x] >= seq[x + 1]:
            return False
    return True

print(is_increasing([1, 2, 3, 4, 5]))
print(is_increasing([1]))
print(is_increasing([5, 6, -10]))
print(is_increasing([1, 1, 1, 1]))
