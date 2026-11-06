
def ceilTheFloor(nums, target):
    n    = len(nums)
    low  = 0
    high = n - 1

    floor, ceil = -1, -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return [nums[mid], nums[mid]]
        
        elif nums[mid] < target:
            floor = nums[mid]
            low = mid + 1

        else:
            ceil = nums[mid] 
            high = mid - 1

    return [floor, ceil]

nums = [3,4,4,4,8,9,9,10,12,12,14,15]
target = 20
print(ceilTheFloor(nums, target))


'''
Time  Complexity - O(log 2 (N))
Space Complexity - O(1)
'''

