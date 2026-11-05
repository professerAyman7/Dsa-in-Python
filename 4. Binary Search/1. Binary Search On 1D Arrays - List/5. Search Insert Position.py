
def search(nums, target):
    n    = len(nums)
    low  = 0
    high = n - 1

    lowerBoundIndex = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lowerBoundIndex = mid
            high = mid - 1
        else:
            low  = mid + 1

    return lowerBoundIndex

nums   = [1,3,4,5,8,9,14,15,19,20,21]
target = -1

print(search(nums, target))


'''
Time  Complexity - O(log 2 (N))
Space Compelxity - O(!1)
'''
