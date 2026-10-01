# What is the brute soltuion??
def twoSum(nums, target):
    mydictionary = {}
    for i in range(0, len(nums)):
        findNumber = target - nums[i]

        if findNumber in mydictionary:
            return [mydictionary[findNumber], i]
        mydictionary[nums[i]] = i

nums = [5,9,1,2,4,15,6,3]
target = 13
print(twoSum(nums, target))


'''
Time  Complexity - O(n)
Space Complexity - O(n)
'''