def is_an_bn(word):
    num_of_a = 0
    num_of_b = 0
    flag = True
    word = word.lower()
    for char in range(0, len(word)):
        if flag:
            if word[char] == 'a':
                num_of_a += 1
            if word[char] == 'b':
                num_of_b += 1
                flag = False
        else:
            if word[char] == 'a':
                return False
            if word[char] == 'b':
                num_of_b += 1
    return num_of_a == num_of_b
