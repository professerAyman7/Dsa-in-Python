# Iterative Solution

def binarySearch(nums, target):
    n    = len(nums)
    low  = 0
    high = n - 1

    # Till this we have to loop
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

nums   = [2, 4, 6, 7, 9, 11, 18, 19]
target = 13

print(binarySearch(nums, target))


'''
Time  Complexity - O(log 2 (N)) - N is the number of elements in list
Space Complexity - O(1)
'''
