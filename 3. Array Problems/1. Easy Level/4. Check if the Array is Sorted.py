def sortedArray(nums):
    for i in range(0, len(nums)-1):
        if nums[i+1] < nums[i]:
            return False
    return True

# nums = [1,2,5,8,3,10,14,15]
nums = [3,5,6,8,9,10,20]
print(sortedArray(nums))


'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''