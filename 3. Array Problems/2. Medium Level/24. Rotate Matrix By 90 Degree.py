# Optimul Solution
def rotate(matrix):
    n = len(matrix)

    # Transpose
    for i in range(0, n-1):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # How to write the code for this?
    for i in range(0, n):
        matrix[i].reverse()

    # Ignoring This
    for i in range(0, n):
        for j in range(0, n):
            print(matrix[i][j], end = " ")
        print()

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
rotate(matrix)


'''
Time  Complexity - O(N*N) + O(N*N) - O(N*N)
Space Complexity - O(1)
'''