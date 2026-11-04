# Recursive Solution

def binarySearch(nums, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarySearch(nums, mid + 1, high, target)
    else:
        return binarySearch(nums, low, mid - 1, target)

nums   = [2, 4, 6, 7, 9, 11, 18, 19]
n      = len(nums)

low    = 0
high   = n - 1
target = 13

print(binarySearch(nums, low, high, target))


'''
Time  Complexity - O(log 2 (N)) - N is the number of elements in list
Space Complexity - O(N) - Stack Space
'''
