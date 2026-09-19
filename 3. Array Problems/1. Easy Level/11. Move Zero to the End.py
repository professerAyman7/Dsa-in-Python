# Brute Solution
def moveZeros(nums):
    temp = []
    for num in nums:
        if num != 0:
            temp.append(num)
    
    tempLength = len(temp)
    for i in range(0, tempLength):
        nums[i] = temp[i]

    for i in range(tempLength, len(nums)):
        nums[i] = 0

nums = [1,0,2,4,3,0,0,3,5,1]
moveZeros(nums)
print(nums)


'''
Time  Complexity - O(2n) - O(n)
Space Complexity - O(n)
'''