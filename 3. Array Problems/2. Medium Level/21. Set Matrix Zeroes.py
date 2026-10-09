def markInfinity(matrix, row, column):
    # O(N + M)
    r = len(matrix)
    c = len(matrix[0])

    for i in range(0, r):
        if matrix[i][column] != 0:
            matrix[i][column] = float("-inf")

    for j in  range(0, c):
        if matrix[row][j] != 0:
            matrix[row][j] = float("-inf")

def matrixZero(matrix):

    row    = len(matrix)
    column = len(matrix[0])

    # O((N + M) * (N * M))
    for i in range(0, row):
        for j in range(0, column):
            if matrix[i][j] == 0:
                markInfinity(matrix, i, j)

    # O(N * M)
    for i in range(0, row):
        for j in range(0, column):
            if matrix[i][j] == float("-inf"):
                matrix[i][j] = 0

    # Ignoring this!
    for i in range(0, row):
        for j in range(0, column):
            print(matrix[i][j], end = " ")
        print(" ")

matrix = [[7,9,2,3], [20,8,0,10], [29,0,-10,5], [4,14,6,7]]
matrixZero(matrix)


'''
N - Number of rows
M - Number of column
Time  Complexity - O((N + M) * (N * M)) + O(N * M)
Space Complexity - O(1)
'''