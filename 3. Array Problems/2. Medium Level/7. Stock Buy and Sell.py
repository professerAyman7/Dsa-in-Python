# Brute Force - How did sir do?

def stockBuyandSell(nums):
    maximum = 0
    # Why doesnt it say list index out of range!!!
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            maximum = max(nums[j] - nums[i], maximum)

    return maximum

# nums = [8,5,3,2,1]
nums = [7,2,1,5,6,4,8]
print(stockBuyandSell(nums))


'''
Time  Complexity - O(n^2)
Space Complexity - O(1)
'''