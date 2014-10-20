def check_square(sudoku, row, column):
    result = 0
    for num in range(1, 10):
        flag = False
        for rows in range(row, row + 3):
            for columns in range(column, column + 3):
                if num == sudoku[rows][columns]:
                    result += 1
                    flag = True
                    break
            if flag:
                break
    return result == 9


def check_row(sudoku, row):
    result = 0
    for num in range(1, 10):
        for columns in range(0, 9):
            if num == sudoku[row][columns]:
                result += 1
                break
    return result == 9


def check_column(sudoku, column):
    result = 0
    for num in range(1, 10):
        for rows in range(0, 9):
            if num == sudoku[rows][column]:
                result += 1
                break
    return result == 9


def sudoku_solved(sudoku):
    flag_square = False
    flag_rows = False
    flag_columns = False
    flag_rows = check_row(sudoku, 0) and check_row(sudoku, 1)\
        and check_row(sudoku, 2) and check_row(sudoku, 3)\
        and check_row(sudoku, 4) and check_row(sudoku, 5)\
        and check_row(sudoku, 6) and check_row(sudoku, 7)\
        and check_row(sudoku, 8)
    flag_columns = check_column(sudoku, 0) and check_column(sudoku, 1)\
        and check_column(sudoku, 2) and check_column(sudoku, 3)\
        and check_column(sudoku, 4) and check_column(sudoku, 5)\
        and check_column(sudoku, 6) and check_column(sudoku, 7)\
        and check_column(sudoku, 8)
    flag_square = check_square(sudoku, 0, 0) and check_square(sudoku, 3, 0)\
        and check_square(sudoku, 6, 0) and check_square(sudoku, 0, 3)\
        and check_square(sudoku, 3, 3) and check_square(sudoku, 6, 3)\
        and check_square(sudoku, 0, 6) and check_square(sudoku, 3, 6)\
        and check_square(sudoku, 6, 6)
    return flag_square and flag_rows and flag_columns
