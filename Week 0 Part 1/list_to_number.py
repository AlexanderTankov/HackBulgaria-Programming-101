def list_to_number(digits):
    new_number = 0
    for number in digits:
        new_number *= 10
        new_number += number
    return new_number

print(list_to_number([1, 2, 3]))
print(list_to_number([9, 9, 9, 9, 9]))
print(list_to_number([1, 2, 3, 0, 2, 3]))
