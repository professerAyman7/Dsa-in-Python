# Optimal Solution
def missingAndRepeating(nums):
    n         = len(nums)
    sum       = 0
    squareSum = 0

    for num in nums:
        sum       += num
        squareSum += num ** 2

    naturalSum       = (n * (n + 1)) // 2
    naturalSquareSum = (n * ((n + 1) * (2 * n + 1))) // 6

    equation1 = sum       - naturalSum
    equation2 = squareSum - naturalSquareSum

    equation2 = equation2 // equation1

    x = (equation1 + equation2) // 2
    y = x - equation1

    return [x, y]

nums = [3, 5, 4, 2, 1, 1]
print(missingAndRepeating(nums))

'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''