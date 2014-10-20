def count_words(arr):
    result = {}
    for word in arr:
        count = 0
        for same_word in arr:
            if(word == same_word):
                count += 1
        result[word] = count
    return result


def unique_words_count(arr):
    return len(count_words(arr))
