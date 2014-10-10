def biggest_difference(arr):
    less_num = arr[0]
    biggest_num = arr[0]
    less_num_idx = 0
    biggest_num_idx = 0
    sum = 0
    for num in arr:
        if(num < less_num):
            less_num = num
            less_num_idx = sum
        elif(num > biggest_num):
            biggest_num = num
            biggest_num_idx = sum
        sum += 1
    if less_num_idx < biggest_num_idx:
        return arr[less_num_idx] - arr[biggest_num_idx]
    else:
        return arr[biggest_num_idx] - arr[less_num_idx]

print(biggest_difference([1, 2]))
print(biggest_difference([1, 2, 3, 4, 5]))
print(biggest_difference([-10, -9, -1]))
print(biggest_difference(range(100)))
