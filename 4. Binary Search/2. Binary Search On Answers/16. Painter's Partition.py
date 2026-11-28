# Optimal Solution
class Solution:
    def painterValid(self, nums, k, mid):
        painterCount = 1
        currentTime  = 0
        for x in nums:
            if currentTime + x > mid:
                painterCount += 1
                currentTime   = x
            else:
                currentTime += x
        return painterCount
    def check(self, nums, k):
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2

            painters = self.painterValid(nums, k, mid)
            if painters <= k:
                high = mid - 1
            else:
                low  = mid + 1

        return low

s = Solution()
nums = [10,20,30,40]
k = 2

print(s.check(nums, k))