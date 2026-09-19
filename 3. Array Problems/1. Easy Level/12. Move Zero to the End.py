# Optimal Solution - how sir did
def moveZeros(nums):
    if len(nums) == 1:
        return
    
    for i in range(0, len(nums)):
        if nums[i] == 0:
            j = i + 1
            while j < len(nums):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j += 1

nums = [1,0,2,4,3,0,0,3,5,1]
moveZeros(nums)
print(nums)
