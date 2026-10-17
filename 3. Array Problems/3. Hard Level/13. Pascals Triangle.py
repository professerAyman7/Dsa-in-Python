# Given any nth row, print the whole row - Optimal Solution
# Do this question again

def wholeRow(n):
    answer = 1
    print(answer, end = " ")

    for i in range(1, n):
        answer  *= (n - i)
        answer //= (i)
        print(answer, end = " ")

row = 5
wholeRow(row)

'''
Time  Complexity - O(row)
Space Complexity - O(1)
'''