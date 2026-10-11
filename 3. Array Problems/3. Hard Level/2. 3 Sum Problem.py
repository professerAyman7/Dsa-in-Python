# Better Solution
def threeSum(nums):
    n        = len(nums)
    myAnswer = set()
    for i in range(0, n):
        mySet = set()
        for j in range(i+1, n):
            k = -(nums[i] + nums[j])
            if k in mySet:
                answer = [nums[i], nums[j], k]
                # Not counting sort because only 3 elements 
                answer.sort()
                myAnswer.add(tuple(answer))
            mySet.add(nums[j])

    return [list(answer) for answer in myAnswer]

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

'''
Time  Complexity - O(n^2)
Space Complexity - O(n) + O(number of triplets)
'''