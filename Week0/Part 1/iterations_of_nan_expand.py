from count_substrings import count_substrings


def iterations_of_nan_expand(expanded):
    str = "Not"
    if expanded == "":
        return 0
    elif expanded == "Not a NaN":
        return 1
    elif count_substrings(expanded, str) != 0:
        return count_substrings(expanded, str)
    else:
        return False
