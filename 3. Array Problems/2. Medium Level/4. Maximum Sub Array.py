# Brute Solution
def subArray(nums):
    maximum = float("-inf")

    for i in range(0, len(nums)):
        # Why did sir say sum = 0 was wrong?
        sum = 0
        for j in range(i, len(nums)):
            sum     = sum + nums[j]
            maximum = max(sum, maximum)

    return maximum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(subArray(nums))

'''
Time  Complexity - O(n^2)
Space Complexity - O(1)
'''