
def lowerBound(nums, target):
    n    = len(nums)
    low  = 0
    high = n - 1

    # Don't take it -1 take it n
    lowerBoundIndex = n

    while low <= high:
        mid = (low + high) // 2

        # NOTE

        if nums[mid] >= target:
            lowerBoundIndex = mid
            high = mid - 1
        else:
            low  = mid + 1

    return lowerBoundIndex

nums   = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target = 4

print(lowerBound(nums, target))


'''
Time  Complexity - O(log 2 (N))
Space Complexity - O(1)
'''


