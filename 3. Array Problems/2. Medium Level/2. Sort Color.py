# Better Solution
def sortColor(nums):
    countZero = 0
    countOne  = 0
    countTwo  = 0

    for num in nums:
        if   num == 0:
            countZero += 1
        elif num == 1:
            countOne  += 1
        else:
            countTwo  += 1

    # int has no length
    for i in range(0, countZero):
        nums[i] = 0
    for i in range(countZero, countZero+countOne):
        nums[i] = 1
    for i in range(countOne+countZero, countZero+countOne+countTwo):
        nums[i] = 2

nums = [1,0,0,2,1,2,2,0,1,2]
sortColor(nums)
print(nums)

'''
Time  Complexity - O(n+n) - O(n)
Space Complexity - O(1)
'''