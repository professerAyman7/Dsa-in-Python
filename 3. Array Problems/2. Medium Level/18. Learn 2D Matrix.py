# Is all this calculated only on square matrix?
def reverseDiagonal(matrix):
    rows   = len(matrix)
    column = len(matrix[0])
    for i in range(0, rows):
        for j in range(0, column):
            if (i + j ) == rows - 1:
                print(matrix[i][j], end = " ")
            else:
                print("*", end = " ")
        print(" ")

matrix = [[5, 1, 8], [7, 6, 3], [2, 1, 9]]
reverseDiagonal(matrix)