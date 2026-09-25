def singleNumber(nums):
    mydictionary = {}
    for num in nums:
        mydictionary[num] = mydictionary.get(num, 0) +1

    for k,v in mydictionary.items():
        if v == 1:
            return k

nums = [4,1,2,1,2]
print(singleNumber(nums))


'''
Time  Complexity - O(n)
Space Complexity - O(n)
'''