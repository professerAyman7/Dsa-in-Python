def mergeSort(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
    
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1

    return result

def mergeSorting(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    leftArray  = nums[ : mid]
    rightArray = nums[mid : ]

    left  = mergeSorting(leftArray)
    right = mergeSorting(rightArray)

    return mergeSort(left, right)

nums = [3,1,2,4,1,5,2,6,4]
print(mergeSorting(nums))
print(nums)

'''
Returns a new list
Time  Complexity - O(N log2(N))
Space Complexity - O(N)
'''