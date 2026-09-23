# How sir did?
def maximum(nums):
    count    = 0
    maxCount = 0
    for num in nums:
        if num == 1:
            count += 1
            if count > maxCount:
                maxCount = count
        else:
            # Why did sir did "max" here?
            count = 0

    return maxCount
nums = [1,1,0,1,0,1,1,1,1,0,1,1,1,1,1]
print(maximum(nums))


'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''