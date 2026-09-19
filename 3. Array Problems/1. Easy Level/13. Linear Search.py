def linearSearch(nums, target):
    for i in range(0, len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = [10,10,20,30,40,50,60,70]
print(linearSearch(nums, 10))


'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''