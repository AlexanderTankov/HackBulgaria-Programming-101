def is_increasing(seq):
    for x in range(0, len(seq) - 1):
        if seq[x] >= seq[x + 1]:
            return False
    return True
