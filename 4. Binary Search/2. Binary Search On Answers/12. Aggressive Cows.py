
# Brute Solution
class Solution:
    def canWePlace(self, stalls, cows, x):
        n         = len(stalls)
        countCows = 1
        lastCow   = stalls[0]
        # Time Complexity - O(n)
        for y in range(1, n):
            if stalls[y] - lastCow >= x:
                countCows += 1
                lastCow    = stalls[y]
            if countCows  >= cows:
                return True
        return False

        
    def valid(self, stalls, cows):
        n = len(stalls)
        maxDistance = stalls[n - 1] - stalls[0]
        # Time Complexity - O(n * (maxDistance))
        for x in range(1, maxDistance + 1):
            if self.canWePlace(stalls, cows, x):
                continue
            else:
                return x - 1
        return maxDistance

s      = Solution()
stalls = [0,3,4,7,9,10]
cows   = 2

# Time Complexity - O(n log n)
stalls.sort()
print(s.valid(stalls, cows))


'''
Time  Complexity - O(n log n + (n * maxDistance))
Space Complexity - O(1)
'''



