y = 5
x = 4
matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0]]


def paths(row_index, col_index, count):
    global current_longest
    matrix[row_index][col_index] = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if not (i == 0 and j == 0):
                next_row, next_col = row_index + i, col_index + j
                if (0 <= next_row < y) & (0 <= next_col < x):
                    if matrix[next_row][next_col] == 1:
                        count = paths(row_index + i, col_index + j, count + 1)
                    else:
                        if count > current_longest:
                            current_longest = count
    return count


current_longest = 0
for row_index, row in enumerate(matrix):
    for column_index, location in enumerate(row):
        if location == 1:
            paths(row_index, column_index, 1)
print(current_longest)
