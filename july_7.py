y = 5   # matrix height
x = 4   # matrix width
matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0]]


def paths(row_index, col_index, count):
    global current_longest  # global keyword lets us assign to global var
    matrix[row_index][col_index] = 0    # set current loc to 0 to avoid double counting
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            next_row, next_col = row_index + i, col_index + j   # indices of next loc to look at
            if (0 <= next_row < y) & (0 <= next_col < x):   # check that next loc is inside matrix
                if matrix[next_row][next_col] == 1:     # should we call our recursive function again?
                    count = paths(row_index + i, col_index + j, count + 1)
                else:
                    if count > current_longest:     # is this the largest area we've found?
                        current_longest = count
    return count


current_longest = 0

# looking through matrix for a '1' to start counting at
for row_index, row in enumerate(matrix):
    for column_index, location in enumerate(row):
        if location == 1:
            paths(row_index, column_index, 1)

print(current_longest)
