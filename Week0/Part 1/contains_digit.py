def contains_digit(number, digit):
    while(number != 0):
        number_digit = number % 10
        number //= 10
        if number_digit == digit:
            return True
    return False
