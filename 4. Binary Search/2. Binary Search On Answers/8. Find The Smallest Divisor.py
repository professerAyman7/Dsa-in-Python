
import math
class Solution:
    def check(self, nums, threshold, n):
        sum = 0
        # Time Complexity - O(n)
        for x in nums:
            sum += math.ceil(x / n)
        return sum <= threshold

    def valid(self, nums, threshold):
        # Time Complexity of these two has been ignoring
        minPoint = min(nums)
        maxPoint = max(nums)

        # Time Complexity - O(n * (max - min))
        for x in range(minPoint, maxPoint + 1):
            if self.check(nums, threshold, x) == True:
                return x

s    = Solution()
nums = [1,9,5,2]
threshold = 6

print(s.valid(nums, threshold))


'''
Time  Complexity - O(n * (max - min))
Space Complexity - O(1)
'''



