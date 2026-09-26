def majorityElement(nums):
    myDictionary = {}
    for num in nums:
        myDictionary[num] = myDictionary.get(num, 0) + 1

    for k, v in myDictionary.items():
        if v > (len(nums)/2):
            return k

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))


'''
Time  Complexity - O(n)
Space Complexity - O(n)
'''