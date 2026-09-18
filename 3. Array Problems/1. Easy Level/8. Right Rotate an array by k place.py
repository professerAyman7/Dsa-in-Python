# Brute Solution
def rotate(nums, k):
    for _ in range(0, k % len(nums)):
        popElement = nums.pop()
        nums.insert(0, popElement)

nums = [3,9,5,6,7,2]
k = 6
rotate(nums, k)
print(nums)


'''
Time  Complexity - O(r*n) - r is the number of rotation  
Space Complexity - O(1)
'''