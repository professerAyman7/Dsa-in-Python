def insertionSort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j   = i-1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

nums = [5,8,1,6,9,2,4]
insertionSort(nums)
print(nums)


'''
Time  Complexity - O((n(n-1))/2) - O(n**2)
Space Complexity - O(1)
'''