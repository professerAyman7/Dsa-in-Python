def missingNumber(nums):
    myDict = {}
    for i in range(0, len(nums) + 1):
        myDict[i] = 0

    for num in nums:
        myDict[num] = 1

    for k, v in myDict.items():
        if v == 0:
            return k

nums = [1,0,3,2]
print(missingNumber(nums))


'''
Time  Complexity - O(3n) - O(n)
Space Complexity - O(n)
'''