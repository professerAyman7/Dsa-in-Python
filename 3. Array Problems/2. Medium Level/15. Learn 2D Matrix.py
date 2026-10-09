# Print the upper triangle
def upper(matrix):
    rows   = len(matrix)
    column = len(matrix[0])
    for i in range(0, rows):
        for j in range(0, column):
            if (i <= j):
                print(matrix[i][j], end = " ")
            else:
                print("*", end = " ")
        print(" ")

matrix = [[5, 1, 8], [7, 6, 3], [2, 1, 9]]
upper(matrix)