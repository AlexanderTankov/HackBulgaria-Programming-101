def prepare_meal(number):
    temp_result_spam = ""
    temp_result_eggs = ""
    count_spam = 0
    if number == 5:
        return "eggs"
    if number % 5 == 0:
        temp_result_eggs += "end eggs"
        number //= 5
    for degree in range(2, number):
        temp_num = 1
        for times in range(1, degree):
            temp_num *= 3
        if temp_num > number:
            break
        else:
            count_spam += 1
    for time_spam in range(0, count_spam):
        temp_result_spam += "spam "
    return temp_result_spam + temp_result_eggs

print(prepare_meal(5))
print(prepare_meal(15))
print(prepare_meal(45))
