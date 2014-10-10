def count_substrings(haystack, needle):
    count = 0
    temp = 0
    result = 0
    for symbol_haystack in range(0, len(haystack)):
        for symbol_needle in range(temp, len(needle)):
            if haystack[symbol_haystack] == needle[symbol_needle]:
                count += 1
                temp += 1
                if count == len(needle):
                    result += 1
                    count = 0
                    temp = 0
            break
    return result


def iterations_of_nan_expand(expanded):
    str = "Not"
    if expanded == " ":
        return 0
    elif expanded == "Not a NaN":
        return 1
    elif count_substrings(expanded, str) != 0:
        return count_substrings(expanded, str)
    else:
        return False


print(iterations_of_nan_expand(" "))
print(iterations_of_nan_expand("Not a NaN"))
print(iterations_of_nan_expand("Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN"))
print(iterations_of_nan_expand("Show these people!"))
