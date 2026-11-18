
# Optimal Solution

import math
class Solution:
    def calculateHour(self, piles, hourRate):
        totalHour = 0
        # Time Complexity - O(n)
        for x in piles:
            totalHour = totalHour + math.ceil(x/hourRate)
        return totalHour

    def valid(self, piles, securityHour):
        maxNumber = max(piles)
        low       = 0
        high      = maxNumber

        # Time Complexity - O(n * (log 2 (max(piles))))
        while low <= high:
            mid = (low + high) // 2
            totalHourConsumed = self.calculateHour(piles, mid)
            if totalHourConsumed <= securityHour:
                high = mid - 1
            else:
                low  = mid + 1

        return low

s            = Solution()
piles        = [3, 6, 7, 11]
securityHour = 8

print(s.valid(piles, securityHour))


'''
Time  Complexity - O(n * (log 2 (max(piles))))
Space Complexity - O(1)
'''
