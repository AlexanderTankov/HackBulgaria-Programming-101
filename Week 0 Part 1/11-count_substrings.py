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

print(count_substrings("This is a test string", "is"))
print(count_substrings("babababa", "baba"))
print(count_substrings("Python is awesome language to program in!", "o"))
print(count_substrings("We have nothing in common!", "really?"))
print(count_substrings("This is this and that is this", "this"))
