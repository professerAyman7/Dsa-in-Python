def rightRotate(nums):
    # lastElement = nums[-1]
    lastElement = nums[len(nums) - 1]
    
    for i in range(len(nums)-2, -1, -1):
        nums[i+1] = nums[i]
    nums[0] = lastElement
    
    print(nums)

nums = [7,5,-2,3,9,0,6,10]
rightRotate(nums)


'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''