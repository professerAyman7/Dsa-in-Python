# Brute Solution

def sortedArray(nums):
    frequencyMap = {}
    for num in nums:
        frequencyMap[num] = 0

    j = 0
    for k in frequencyMap:
        nums[j] = k
        j += 1
    
    # print(nums)
    return j

nums = [1,1,1,2,3,4,4,7,9,9,9,10]
print(sortedArray(nums))


'''
Time  Complexity - O(n+n) - O(n)
Space Complexity - O(n)
'''