
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
        low  = min(nums)
        high = max(nums)

        while low <= high:
            mid = (low + high) // 2
            if self.check(nums, threshold, mid) == True:
                high   = mid - 1
            else:
                low    = mid + 1
        return low


s    = Solution()
nums = [1,9,5,2]
threshold = 6

print(s.valid(nums, threshold))


'''
Time  Complexity - O(n * (log 2 (high - low)))
Space Complexity - O(1)
'''




