def is_equal_list(list):
    if list == []:
        return False
    temp = list[0]
    for x in list:
        if x != temp:
            return False
    return True


def sqrt(num):
    for x in range(1, num // 2):
        if x * x == num:
            return x
    return -1


def magic_square(matrix):
    sum_fw_diagonal = 0
    sum_bw_diagonal = 0
    sum_row = []
    sum_column = []
    temp_list = []
    for row in range(0, len(matrix)):
        sum = 0
        for column in range(0, len(matrix)):
            sum += matrix[row][column]
            if column == row:
                sum_fw_diagonal += matrix[row][column]
            if column + row == len(matrix) - 1:
                sum_bw_diagonal += matrix[row][column]
            temp_list.append(matrix[row][column])
        sum_row.append(sum)
    for num in range(0, sqrt(len(temp_list))):
        moment_sum_col = temp_list[num]
        mom_pos = num
        for x in range(sqrt(len(temp_list)), len(temp_list)):
            if (x - mom_pos) % sqrt(len(temp_list)) == 0:
                moment_sum_col += temp_list[x]
        sum_column.append(moment_sum_col)
    return (sum_fw_diagonal == sum_bw_diagonal) and \
        (sum_fw_diagonal == sum_row[0]) and is_equal_list(sum_row)\
        and sum_row[0] == sum_column[0] and is_equal_list(sum_column)
