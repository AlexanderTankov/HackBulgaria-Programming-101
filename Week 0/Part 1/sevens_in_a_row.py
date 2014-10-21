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
