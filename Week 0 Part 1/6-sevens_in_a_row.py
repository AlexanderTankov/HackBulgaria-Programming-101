def sevens_in_a_row(arr, n):
    count = 0
    flag = False
    for number in range(0, len(arr)):
        if arr[number] == 7:
            count += 1
            if count == n:
                flag = True
        else:
            count = 0
    return flag

print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
print(sevens_in_a_row([1, 7, 1, 7, 7], 4))
print(sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))
print(sevens_in_a_row([7, 2, 1, 6, 2], 1))
