# Given any nth row, print the whole row - Brute Solutin
# Do this question again

# If the row starts from 0
# If the row starts with 1 - then (row - 1)


def nCr(n, r):
    result = 1
    for i in range(r):
        result  *= (n - i)
        result //= (i + 1)
    return result

def wholeRow(n):
    # Why does the loop start from 0 here???
    for i in range(n + 1):
        print(nCr(n, i), end = " ")

row = 5
n   = row - 1
wholeRow(n)

'''
Time  Complexity - O(n * column) or O(n * r)
Space Complexity - O(1)
'''