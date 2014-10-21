def count_vowels(string):
    list_with_vowels = "aeiouy"
    result = 0
    string = string.lower()
    for x in range(0, len(string)):
        for y in range(0, len(list_with_vowels)):
            if(string[x] == list_with_vowels[y]):
                result += 1
    return result
