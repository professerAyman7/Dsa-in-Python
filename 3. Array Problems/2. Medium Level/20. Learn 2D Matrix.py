# Transpose of a matrix - for any matrix
def transpose(matrix):
    rows   = len(matrix)
    column = len(matrix[0])
    # Revise this
    result = [[0] * rows for _ in range(0, column)]
    newRows = len(result)
    newColumn = len(result[0])

    for i in range(0, rows):
        for j in range(0, column):
            print(matrix[i][j], end = " ")
        print()

    print()

    for i in range(0, rows):
        for j in range(0, column):
            result[j][i] = matrix[i][j]

    for i in range(0, newRows):
        for j in range(0, newColumn):
            print(result[i][j], end = " ")
        print()


matrix = [[5, 9, 1], [2, 3, 7]]
transpose(matrix)