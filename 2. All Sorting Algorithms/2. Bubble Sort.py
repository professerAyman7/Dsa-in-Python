def bubbleSort(nums):
    n = len(nums)
    for i in range(n-2, -1, -1):
        isSwap = False
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                isSwap = True
        if isSwap == False:
            break # Or return


nums = [5,8,1,6,9,2,4]
bubbleSort(nums)
print(nums)


'''
This is for average and worst case
Time  Complexity - O((n(n-1))/2) - O(n**2)
Space Complexity - O(1)

For the best case still it will be the same it will not swap but it will check so we need to do some changes!!!
That is why we added the isSwap
So in the best case the Time Complexity will be: O(n)
and the Space Complexity will be: O(1)
'''