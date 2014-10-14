def simplify_fraction(fraction):
    fst_elem = fraction[0]
    snd_elem = fraction[1]
    for num in range(1, fst_elem + 1):
        if (fst_elem % num == 0) and (snd_elem % num == 0):
            fst_elem //= num
            snd_elem //= num
    return (fst_elem, snd_elem)


print(simplify_fraction((3, 9)))
print(simplify_fraction((1, 7)))
print(simplify_fraction((4, 10)))
print(simplify_fraction((63, 462)))
