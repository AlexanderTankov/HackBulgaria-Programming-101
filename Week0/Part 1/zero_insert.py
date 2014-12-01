def zero_insert(n):
    temp = n
    flag = False
    while not flag:
        temp_list = []
        new_number = temp
        while temp != 0:
            temp_list.append(temp % 10)
            temp //= 10
        temp_list.reverse()
        for x in range(0, len(temp_list) - 1):
            if temp_list[x] == temp_list[x + 1]:
                temp_list.insert(x + 1, 0)
            elif ((temp_list[x] + temp_list[x + 1]) % 10) == 0:
                temp_list.insert(x + 1, 0)
        for i in range(0, len(temp_list)):
            temp *= 10
            temp += temp_list[i]
        if new_number == temp:
            flag = True
    return temp
