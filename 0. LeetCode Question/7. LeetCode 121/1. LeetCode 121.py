def bestTime(prices):
    maxProfit = 0
    profit    = float("-inf")
    minPrice  = float("inf")

    for price in prices:
        if price < minPrice:
            minPrice = price

        # We dont need to check if we can update it directly
        if price > minPrice:
            profit = price - minPrice
            
        if profit > maxProfit:
            maxProfit = profit

    return maxProfit

prices = [7,1,5,3,6,4]
print(bestTime(prices))


'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''