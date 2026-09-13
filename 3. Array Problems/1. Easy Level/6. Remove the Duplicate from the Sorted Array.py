# Optimul Solution

def sorted(nums):

    if len(nums) == 1:
        return 1
    if len(nums) == 0:
        return 0
    
    # When we wrote in the same line why didnt it worked?
    i = 0
    j = i+1 

    # Why not for loop?
    while j < len(nums):
        if nums[j] != nums[i]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1

    # print(nums)
    return i + 1
nums = [1,1,1,2,3,4,4,7,9,9,9,10]
print(sorted(nums))


'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''