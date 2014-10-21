def list_to_number(digits):
    new_number = 0
    for number in digits:
        new_number *= 10
        new_number += number
    return new_number
