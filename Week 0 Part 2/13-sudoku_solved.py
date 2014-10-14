def sudoku_square(sudoku, row, column):
    result = 0
    for num in range(1, 10):
        for rows in range(row, row + 3):
            for columns in range(column, column + 3):
                if num == sudoku[rows][columns]:
                    result += 1
                    break
    return result == 9


def is_equal_list(list):
    if list == []:
        return False
    temp = list[0]
    for x in list:
        if x != temp:
            return False
    return True



def sudoku_solved(sudoku):
    sum_square = True
    sum_rows = []
    sum_columns = []
    for rows in range(0, 9):
        temp_sum_columns = 0
        for columns in range(0, 9):
            temp_sum_columns += sudoku[rows][columns]
        sum_columns.append(temp_sum_columns)
    for column in range(0, 9):
        temp_sum_rows = 0
        for row in range(0, 9):
            temp_sum_rows += sudoku[row][column]
        sum_rows.append(temp_sum_rows)
    sum_square = sudoku_square(sudoku, 0, 0)
    sum_square = sudoku_square(sudoku, 3, 0)
    sum_square = sudoku_square(sudoku, 6, 0)
    sum_square = sudoku_square(sudoku, 0, 3)
    sum_square = sudoku_square(sudoku, 3, 3)
    sum_square = sudoku_square(sudoku, 6, 3)
    sum_square = sudoku_square(sudoku, 0, 6)
    sum_square = sudoku_square(sudoku, 3, 6)
    sum_square = sudoku_square(sudoku, 6, 6)
    return sum_square and is_equal_list(sum_rows) and is_equal_list(sum_columns)


print(sudoku_solved([
[4, 5, 2, 3, 8, 9, 7, 1, 6],
[3, 8, 7, 4, 6, 1, 2, 9, 5],
[6, 1, 9, 2, 5, 7, 3, 4 ,8],
[9, 3, 5, 1, 2, 6, 8, 7, 4],
[7, 6, 4, 9, 3, 8, 5, 2, 1],
[1, 2, 8, 5, 7, 4, 6, 3, 9],
[5, 7, 1, 8, 9, 2, 4, 6, 3],
[8, 9, 6, 7, 4, 3, 1, 5 ,2],
[2, 4, 3, 6, 1, 5, 9, 8, 7]
]))
print(sudoku_solved([
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9]
]))