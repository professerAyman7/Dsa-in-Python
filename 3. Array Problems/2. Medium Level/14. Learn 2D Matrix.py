'''
matrix = [[3,8,9,2,1,4], [7,5,-1,-6,9,3], [2,6,-2,1,-1,-7]]
rows   = len(nums)
column = len(nums[0])
'''

# Iteration
matrix = [[3,8,9,2,1,4], [7,5,1,6,9,3], [2,6,2,1,1,7]]
rows   = len(matrix)
column = len(matrix[0])
for i in range(0, rows):
    for j in range(0, column):
        print(matrix[i][j], end = " ")
    # What does this line does 
    # print()
    print(" ")