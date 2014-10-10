def zero_insert(n):
    list = []
    while n != 0:
        list.append(n % 10)
        n //= 10
    list.reverse()
    for x in range(0, len(list) - 1):
        if list[x] == list[x + 1]:
            list.insert(x + 1, 0)
        elif ((list[x] + list[x + 1]) % 10) == 0:
            list.insert(x + 1, 0)
    for i in range(0, len(list)):
        n *= 10
        n += list[i]
    return n

print(zero_insert(116457))
print(zero_insert(55555555))
print(zero_insert(1))
print(zero_insert(6446))
