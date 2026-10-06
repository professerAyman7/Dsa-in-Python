def rearrange(nums):
    # Time Complexity of this also?
    result = [0] * len(nums)
    positive, negative = 0, 1
    for num in nums:
        if num >= 0:
            result[positive] = num
            positive += 2
        else:
            result[negative] = num
            negative += 2

    return result

# What if there is a zero from before in the array and we dont use >= 
nums = [5, 10, -3, -1, -10, 6]
print(rearrange(nums))


'''
Time  Complexity - O(n)
Space Complexity - O(n) - but we return that so if we ignore that - O(1)
'''