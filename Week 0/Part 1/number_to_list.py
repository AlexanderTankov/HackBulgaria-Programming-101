def number_to_list(n):
    list = []
    while n != 0:
        list.append(n % 10)
        n //= 10
    list.reverse()
    return list

print(number_to_list(123))
print(number_to_list(99999))
print(number_to_list(123023))
