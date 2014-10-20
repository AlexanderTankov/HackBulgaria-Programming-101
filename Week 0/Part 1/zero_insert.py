def zero_insert(n):
    temp = n
    flag = False
    while not flag:
        list = []
        new_number = temp
        while temp != 0:
            list.append(temp % 10)
            temp //= 10
        list.reverse()
        for x in range(0, len(list) - 1):
            if list[x] == list[x + 1]:
                list.insert(x + 1, 0)
            elif ((list[x] + list[x + 1]) % 10) == 0:
                list.insert(x + 1, 0)
        for i in range(0, len(list)):
            temp *= 10
            temp += list[i]
        if new_number == temp:
            flag = True
    return temp


print(zero_insert(116457))
print(zero_insert(55555555))
print(zero_insert(1))
print(zero_insert(6446))
