def count_consonants(string):
    list_with_consonants = "bcdfghjklmnpqrstvwxz"
    result = 0
    string = string.lower()
    for x in range(0, len(string)):
        for y in range(0, len(list_with_consonants)):
            if(string[x] == list_with_consonants[y]):
                result += 1
    return result
