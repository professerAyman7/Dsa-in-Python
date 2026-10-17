# First Variation - Given the row and column, print the element
# Do this question again

# If the row and column start with 0
# If the row and column start with 1 - then [n = row - 1 and r = column - 1]

# Why can't we write nCr(n-1, r-1)??
def nCr(n, r):
    result = 1
    for i in range(r):
        result  *= (n - i)
        result //= (i + 1)
    return result

row    = 5
column = 3

n = row
r = column
print(nCr(n, r))

'''
Time  Complexity - O(r) or O(column)
Space Complexity - O(1)
'''