# O(n) time | O(n) space
def spiralTraverse(array):
    result = []
    if len(array) == 0:
        return result
    start_row = 0
    end_row = len(array) - 1
    start_col = 0
    end_col = len(array[0]) - 1

    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])

        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_col])

        for col in reversed(range(start_col, end_col)):
            result.append(array[end_row][col])

        for row in reversed(range(start_row + 1, end_row)):
            result.append(array[row][start_col])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return result


print(spiralTraverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))


# O(n) time | O(n) space
def spiralTraverseRecursive(array):
    result = []
    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result


def spiralFill(array, start_row, end_row, start_col, end_col, result):
    if start_row > end_row or start_col > end_col:
        return
    for col in range(start_col, end_col + 1):
        result.append(array[start_row][col])

    for row in range(start_row + 1, end_row + 1):
        result.append(array[row][end_col])

    for col in reversed(range(start_col, end_col)):
        result.append(array[end_row][col])

    for row in reversed(range(start_row + 1, end_row)):
        result.append(array[row][start_col])

    spiralFill(array, start_row + 1, end_row - 1, start_col + 1, end_col - 1, result)


print(spiralTraverseRecursive([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))


# def spiralOrder(self, matrix):
#     return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])

# print(spiralOrder(self, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))


def spiralOrder(matrix):
    res = []
    if len(matrix) == 0:
        return res
    row_begin = 0
    col_begin = 0
    row_end = len(matrix) - 1
    col_end = len(matrix[0]) - 1
    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end + 1):
            res.append(matrix[row_begin][i])
        row_begin += 1
        for i in range(row_begin, row_end + 1):
            res.append(matrix[i][col_end])
        col_end -= 1
        if row_begin <= row_end:
            for i in range(col_end, col_begin - 1, -1):
                res.append(matrix[row_end][i])
            row_end -= 1
        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                res.append(matrix[i][col_begin])
            col_begin += 1
    return res


print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
