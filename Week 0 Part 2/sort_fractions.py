def sort_fractions(fractions):
    result = []
    while len(fractions) != 1:
        min_elem = fractions[0][0] / fractions[0][1]
        pos_min_elem = 0
        for elem in range(1, len(fractions)):
            moment_elem = fractions[elem][0] / fractions[elem][1]
            if moment_elem < min_elem:
                min_elem = moment_elem
                pos_min_elem = elem
        result.append((fractions[pos_min_elem][0], fractions[pos_min_elem][1]))
        del fractions[pos_min_elem]
    result.append(fractions[0])
    return result


print(sort_fractions([(2, 3), (1, 2)]))
print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
