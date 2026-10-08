def leader(nums):
    result = []
    leaderElement = float("-inf")

    for i in range(len(nums)-1, -1, -1):
        if nums[i] > leaderElement:
            result.append(nums[i])
            leaderElement = nums[i]
    return result[::-1]

nums = [16,17,4,3,5,2]
print(leader(nums))


'''
Time  Complexity - O(n) + O(n) - O(2n) - O(n)
Space Complexity - O(1) - if we ignore the result
'''