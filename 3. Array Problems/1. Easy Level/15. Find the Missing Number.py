def missing(nums):
    for i in range(0, len(nums)+1):
        if i not in nums:
            return i

nums = [1,0,3,2]
print(missing(nums))

'''
Time  Complexity - O(n**2)
Space Complexity - O(1)
'''