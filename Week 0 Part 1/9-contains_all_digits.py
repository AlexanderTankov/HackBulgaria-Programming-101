def contains_digits(number, digits):
    for i in digits:
        flag = False
        temp = number
        while temp != 0:
            if temp % 10 == i:
                flag = True
            temp //= 10
        if not flag:
            return False
    return True

print(contains_digits(402123, [0, 3, 4]))
print(contains_digits(666, [6, 4]))
print(contains_digits(123456789, [1, 2, 3, 0]))
print(contains_digits(456, []))
