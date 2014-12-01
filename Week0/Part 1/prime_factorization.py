from is_prime import is_prime


def repetition_in_list(list):
    new_list = []
    for item in list:
        item_in_new_list = item
        pos_of_new_item = 0
        for num in range(0, len(list)):
            if item_in_new_list == list[num]:
                pos_of_new_item += 1
        flag = True
        for items in range(0, len(new_list)):
            if (item_in_new_list, pos_of_new_item) == new_list[items]:
                flag = False
        if flag:
            new_list.append((item_in_new_list, pos_of_new_item))
    return new_list


def prime_factorization(n):
    list = []
    if n == 0:
        return 0
    if n == 1:
        return 1
    while n != 1:
        temp = n
        for x in range(2, n + 1):
            if n % x == 0:
                if is_prime(x):
                    n //= x
                    list.append((x))
            if n != temp:
                break
    return repetition_in_list(list)
