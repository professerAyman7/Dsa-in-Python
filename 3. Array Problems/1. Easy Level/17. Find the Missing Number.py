def missing(nums):
    n = len(nums)
    
    return int((n*(n+1))/2 - sum(nums))

nums = [1,0,3,2]
print(missing(nums))


'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''