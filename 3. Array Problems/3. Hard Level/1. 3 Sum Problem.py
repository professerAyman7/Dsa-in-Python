# Brute Solution
def threeSum(nums):
    n     = len(nums)
    mySet = set()
    # Why not error in list index
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    myList = [nums[i], nums[j], nums[k]]
                    # Not counting sort because only 3 elements 
                    myList.sort()
                    mySet.add(tuple(myList))

    return [list(answer) for answer in mySet]

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

'''
Time  Complexity - O(n^3)
Space Complexity - O(number of triplets)
'''