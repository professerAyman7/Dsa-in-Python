def selectionSort(nums):
    for i in range(0, len(nums)):
        minIndex = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]

nums = [5,7,8,4,1,6,9,2]
selectionSort(nums)
print(nums)

'''
Time  Complexity - O(n**2)
Space Complexity - O(1)
'''