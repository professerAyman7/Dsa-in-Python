# Transpose of a matrix - this is just for square matrix
def transpose(matrix):
    rows   = len(matrix)
    column = len(matrix[0])

    for i in range(0, rows):
        for j in range(0, column):
            print(matrix[j][i], end = " ")
        print(" ")

matrix = [[5, 1, 8], [7, 6, 3], [2, 1, 9]]
transpose(matrix)
