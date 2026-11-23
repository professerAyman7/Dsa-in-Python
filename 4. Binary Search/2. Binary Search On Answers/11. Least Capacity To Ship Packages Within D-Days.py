
# Optimal Solution
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
        low  = max(weight)
        high = sum(weight)

        # Time Complexity - O(n * log 2 (high - low))
        while low <= high:
            mid = (low + high) // 2
            if self.check(weight, mid, days) == True:
                high = mid - 1
            else:
                low  = mid + 1
        return low


s = Solution()
weight = [1,2,3,4,5,6,7,8,9,10]
days   = 5

print(s.daysCheck(weight, days))


'''
Time  Complexity - O(n * log 2 (high - low))
Space Complexity - O(1)
'''




