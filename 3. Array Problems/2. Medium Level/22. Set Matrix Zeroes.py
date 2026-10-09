def matrixZero(matrix):
    row    = len(matrix)
    column = len(matrix[0])

    # How sir did by list comprehension
    rowMatrix    = [0] * row
    columnMatrix = [0] * column

    # O(N * M)
    for i in range(0, row):
        for j in range(0, column):
            if matrix[i][j] == 0:
                rowMatrix[i] = -1
                columnMatrix[j] = -1

    # O(N * M)
    for i in range(0, row):
        for j in range(0, column):
            if rowMatrix[i] == -1 or rowMatrix[j] == -1:
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
Time  Complexity - O(2(N * M)) - O(N * M)
Space Complexity - O(N + M)
'''