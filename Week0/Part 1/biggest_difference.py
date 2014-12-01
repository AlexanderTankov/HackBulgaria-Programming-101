def biggest_difference(arr):
    less_num = arr[0]
    biggest_num = arr[0]
    less_num_idx = 0
    biggest_num_idx = 0
    temp_index = 0
    for num in arr:
        if(num < less_num):
            less_num = num
            less_num_idx = temp_index
        elif(num > biggest_num):
            biggest_num = num
            biggest_num_idx = temp_index
        temp_index += 1
    if less_num_idx < biggest_num_idx:
        return arr[less_num_idx] - arr[biggest_num_idx]
    else:
        return arr[biggest_num_idx] - arr[less_num_idx]
