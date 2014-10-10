def is_int_palindrome(n):
    left_num = 0
    right_num = 0
    if n < 0:
        n *= -1
    if n < 10 and n > 0:
        return True
    temp = n
    sum_of_num = 0
    while temp != 0:
        sum_of_num += 1
        temp //= 10
    for i in range(0, sum_of_num // 2):
        left_num *= 10
        left_num += n % 10
        n //= 10
    if sum_of_num % 2 != 0:
        n //= 10
    right_num = n
    return left_num == right_num


def is_int_palindrome_snd(n):
    new_number = 0
    temp = n
    while n != 0:
        new_number *= 10
        new_number += n % 10
        n //= 10
    return temp == new_number

print(is_int_palindrome(1))
print(is_int_palindrome(42))
print(is_int_palindrome(100001))
print(is_int_palindrome(999))
print(is_int_palindrome(123))

print(is_int_palindrome_snd(1))
print(is_int_palindrome_snd(42))
print(is_int_palindrome_snd(100001))
print(is_int_palindrome_snd(999))
print(is_int_palindrome_snd(123))
