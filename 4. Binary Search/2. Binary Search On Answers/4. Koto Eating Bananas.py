
# Brute Solution

import math
class Solution:
    def calculateHour(self, piles, hourRate):
        totalHour = 0
        # Time Complexity - O(n)
        for x in piles:
            totalHour = totalHour + math.ceil(x/hourRate)
        return totalHour

    def valid(self, piles, securityHour):
        # Doesnt calculating max takes time complexity??
        maxNumber = max(piles)

        # Time  Complexity - O(n * max(piles))
        for i in range(1, maxNumber + 1):
            totalHourConsumed = self.calculateHour(piles, i)

            if totalHourConsumed <= securityHour:
                return i

s            = Solution()
piles        = [3, 6, 7, 11]
securityHour = 8

print(s.valid(piles, securityHour))


'''
Time  Complexity - O(n * max(piles))
Space Complexity - O(1)
'''
