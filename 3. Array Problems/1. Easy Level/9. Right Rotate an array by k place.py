# Better Solution
def rotate(nums, k):
    n = len(nums)
    k = n % k

    nums[:] = nums[n-k:] + nums[:n-k]

nums = [3,9,5,6,7,2]
k = 3
rotate(nums, k)
print(nums)


'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''