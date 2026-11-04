
def upperBound(nums, target):
    n    = len(nums)
    low  = 0
    high = n - 1

    # Don't take it -1 take it n
    upperBoundIndex = n

    while low <= high:
        mid = (low + high) // 2

        # NOTE

        if nums[mid] > target:
            upperBoundIndex = mid
            high = mid - 1
        else:
            low  = mid + 1

    return upperBoundIndex

nums   = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target = 1

print(upperBound(nums, target))


'''
Time  Complexity - O(log 2 (N))
Space Complexity - O(1)
'''


