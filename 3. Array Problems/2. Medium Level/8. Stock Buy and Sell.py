# Optimul Solution - How did sir do?

def stockBuyandSell(nums):
    minPrice  = float("inf")
    maxProfit = 0
    for num in nums:
        if num < minPrice:
            minPrice = num
        else:
            maxProfit = max(maxProfit, num - minPrice)
    return maxProfit

nums = [8,5,3,2,1]
# nums = [7,2,1,5,6,4,8]
print(stockBuyandSell(nums))


'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''