def is_number_balanced(n):
    left_sum = 0
    right_sum = 0
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
        right_sum += n % 10
        n //= 10
    if sum_of_num % 2 != 0:
        n //= 10
    while n != 0:
        left_sum += n % 10
        n //= 10
    return left_sum == right_sum
