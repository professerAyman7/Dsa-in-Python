def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high

    while i < j:
        # Why high-1 and low+1
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        while nums[j] > pivot and j >= low + 1:
            j -= 1

        # Why did we check here
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]

    return j

def quickSort(nums, low, high):
    if low < high:
        setIndex = partition(nums, low, high)
        quickSort(nums, low, setIndex-1)
        quickSort(nums, setIndex+1, high)

nums = [3,1,2,4,7,6,8]
quickSort(nums, 0, len(nums)-1)
print(nums)


'''
# Best and Average case time complexity
Time  Complexity - O(N log N)

# Worst Case
Time  Complexity - O(N * N)

Space Complexity - O(1) - if we remove the stack space
'''