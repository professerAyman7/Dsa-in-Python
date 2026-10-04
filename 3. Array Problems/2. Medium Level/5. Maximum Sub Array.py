# Optimul Solution
def subArray(nums):
    # Dont take variable name sum - python built-in function
    sum     = 0
    maximum = float("-inf")

    for i in range(0, len(nums)):
        sum = sum + nums[i]
        maximum = max(sum, maximum)

        if sum < 0:
            sum = 0

    return maximum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(subArray(nums))


'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''