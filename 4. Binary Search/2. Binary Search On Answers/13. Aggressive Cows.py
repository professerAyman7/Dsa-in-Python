
# Optimal Solution
class Solution:
    def canWePlace(self, stalls, cows, x):
        n = len(stalls)
        countCows = 1
        lastCow = stalls[0]
        # Time Complexity - O(n)
        for y in range(1, n):
            if stalls[y] - lastCow >= x:
                countCows += 1
                lastCow = stalls[y]
            if countCows >= cows:
                return True
        return False

    def valid(self, stalls, cows):
        n = len(stalls)
        low = 1
        high = stalls[n - 1] - stalls[0]

        # Time Complexity - O(n * log 2 (high - low))
        while low <= high:
            mid = (low + high) // 2
            if self.canWePlace(stalls, cows, mid):
                low = mid + 1
            else:
                high = mid - 1
        return high


s = Solution()
stalls = [0, 3, 4, 7, 9, 10]
cows = 2

# Time Complexity - O(n log n)
stalls.sort()
print(s.valid(stalls, cows))


'''
Time  Complexity - O(n log n + (n * log 2 (high - low)))
Space Complexity - O(1)
'''
