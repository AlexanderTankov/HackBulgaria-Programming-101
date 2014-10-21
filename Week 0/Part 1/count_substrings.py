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
            else:
                count = 0
                temp = 0
            break
    return result
