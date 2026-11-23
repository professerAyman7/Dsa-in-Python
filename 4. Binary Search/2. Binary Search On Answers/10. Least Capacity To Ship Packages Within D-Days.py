
# Brute Solution
class Solution:
    def check(self, weight, capacity, days):
        totalDays = 1
        load      = 0
        # Time Complexity - O(n)
        for w in weight:
            if load + w > capacity:
                totalDays += 1
                load       = 0
            load += w
        return totalDays <= days

    def daysCheck(self, weight, days):
        # Ignoring These Time Complexity
        minDays  = max(weight)
        maxDays  = sum(weight)

        # Time Complexity - O(n * (maxDays - minDays))
        for x in range(minDays, maxDays + 1):
            if self.check(weight, x, days) == True:
                return x

s = Solution()
weight = [1,2,3,4,5,6,7,8,9,10]
days   = 5

print(s.daysCheck(weight, days))


'''
Time  Complexity - O(n * (maxDays - minDays))
Space Complexity - O(1)
'''




