# Brute Solution
def rotate(matrix):
    n = len(matrix)

    result = [[0] * n for _ in range(0, n)]

    # O(N * M)
    for i in range(0, n):
        for j in range(0, n):
            result[j][(n - 1) - i] = matrix[i][j]

    # Ignoring This
    for i in range(0, n):
        for j in range(0, n):
            print(result[i][j], end = " ")
        print()

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
rotate(matrix)

'''
Time  Complexity - O(N^2)
Space Complexity - O(N^2) - why this? why not "N + N"
'''